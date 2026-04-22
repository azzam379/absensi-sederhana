# File: backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import siswa, absensi

# Autentikasi koneksi DB dan buat tabel jika belum ada
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Absensi Sederhana API", 
    version="1.0.0",
    description="API untuk manajemen data siswa dan kehadiran."
)

# Tambahkan CORS Middleware untuk mengizinkan website pada HTML (Local)
# mengakses Backend API (development mode: open all)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hubungkan modul Router dengan awalan /api agar Vercel mendeteksinya dengan benar
app.include_router(siswa.router, prefix="/api")
app.include_router(absensi.router, prefix="/api")

@app.get("/api")
def root():
    return {"message": "Service Backend Absensi Sederhana Berjalan dengan Baik"}
