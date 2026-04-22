# File: backend/tests/test_absensi.py
import pytest
from datetime import date

# Pinjam 'client' simulasi API dari file test_siswa
from backend.tests.test_siswa import client 

def test_tambah_absensi():
    # 1. Pertama, buat 1 siswa eksperimen agar ada ID yang bisa diabsen
    siswa_response = client.post(
        "/siswa/",
        json={"nama": "Siti Aminah", "kelas": "XI TKJ 2"}
    )
    siswa_id = siswa_response.json()["id"]

    # 2. Tes menembak API absensi
    today = date.today().isoformat() # Convert "Tahun-Bulan-Tanggal"
    response = client.post(
        "/absensi/",
        json={
            "siswa_id": siswa_id,
            "tanggal": today,
            "status": "Hadir",
            "keterangan": "Tepat waktu"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Hadir"
    assert data["siswa_id"] == siswa_id

def test_gagal_absen_jika_siswa_fiktif():
    today = date.today().isoformat()
    response = client.post(
        "/absensi/",
        json={
            "siswa_id": 9999, # ID Siswa Ngawur / Fiktif
            "tanggal": today,
            "status": "Izin",
            "keterangan": "Sakit"
        }
    )
    # Harus ditolak oleh sistem dan error 404 (Siswa tidak ditemukan)
    assert response.status_code == 404 
