# File: backend/routers/absensi.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/absensi",
    tags=["Absensi"]
)

@router.get("/", response_model=List[schemas.AbsensiResponse])
def get_all_absensi(db: Session = Depends(get_db)):
    return db.query(models.Absensi).all()

@router.post("/", response_model=schemas.AbsensiResponse)
def create_absensi(absensi: schemas.AbsensiCreate, db: Session = Depends(get_db)):
    # Validasi apakah siswa yang diinputkan benar-benar ada di database
    db_siswa = db.query(models.Siswa).filter(models.Siswa.id == absensi.siswa_id).first()
    if not db_siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    
    # model_dump() adalah metode pydantic versi terbaru untuk convert Object ke dict
    db_absensi = models.Absensi(**absensi.model_dump())
    db.add(db_absensi)
    db.commit()
    db.refresh(db_absensi)
    return db_absensi

@router.get("/rekap/{siswa_id}", response_model=schemas.RekapAbsensiSiswa)
def get_rekap_siswa(siswa_id: int, db: Session = Depends(get_db)):
    db_siswa = db.query(models.Siswa).filter(models.Siswa.id == siswa_id).first()
    if not db_siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    # SQLAlchemy relationship secara otomatis akan memuat "absensi" yang terkait
    return db_siswa

@router.get("/filter", response_model=List[schemas.AbsensiResponse])
def filter_absensi_by_tanggal(tanggal: date = Query(...), db: Session = Depends(get_db)):
    absensi_list = db.query(models.Absensi).filter(models.Absensi.tanggal == tanggal).all()
    return absensi_list
