# File: backend/tests/test_siswa.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.main import app
from backend.database import Base, get_db

# 1. Setup Database Khusus Testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_absensi.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Buat ulang semua tabel khusus untuk DB Test
Base.metadata.create_all(bind=engine)

# 3. Timpah koneksi Database Utama dengan DB Test
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# 4. Buat objek pengetes (simulasi browser)
client = TestClient(app)

def test_tambah_siswa():
    response = client.post(
        "/siswa/",
        json={"nama": "Budi Santoso", "kelas": "X RPL 1"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nama"] == "Budi Santoso"
    assert "id" in data

def test_ambil_semua_siswa():
    response = client.get("/siswa/")
    assert response.status_code == 200
    # Pastikan kembalian data berupa List (Array)
    assert isinstance(response.json(), list) 

def test_siswa_tidak_ditemukan():
    # Mengetes cara mengatasi error jika ID yang dicari ngawur
    response = client.delete("/siswa/999")
    assert response.status_code == 404

