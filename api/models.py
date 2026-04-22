# File: backend/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Siswa(Base):
    __tablename__ = "siswa"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    kelas = Column(String)
    
    # Relasi ke tabel absensi
    absensi = relationship("Absensi", back_populates="siswa", cascade="all, delete-orphan")

class Absensi(Base):
    __tablename__ = "absensi"

    id = Column(Integer, primary_key=True, index=True)
    siswa_id = Column(Integer, ForeignKey("siswa.id"))
    tanggal = Column(Date, index=True)
    status = Column(String) # Hadir, Izin, Sakit, Alfa
    keterangan = Column(String, nullable=True)

    siswa = relationship("Siswa", back_populates="absensi")
