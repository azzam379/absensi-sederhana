# File: backend/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional, List

# --- Schema Siswa ---
class SiswaBase(BaseModel):
    nama: str
    kelas: str

class SiswaCreate(SiswaBase):
    pass

class SiswaResponse(SiswaBase):
    id: int

    class Config:
        from_attributes = True

# --- Schema Absensi ---
class AbsensiBase(BaseModel):
    siswa_id: int
    tanggal: date
    status: str
    keterangan: Optional[str] = None

class AbsensiCreate(AbsensiBase):
    pass

class AbsensiResponse(AbsensiBase):
    id: int

    class Config:
        from_attributes = True
        
# --- Schema Rekap/Agregasi (Opsional) ---
class RekapAbsensiSiswa(SiswaResponse):
    absensi: List[AbsensiResponse] = []
