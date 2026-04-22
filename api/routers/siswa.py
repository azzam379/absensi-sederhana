# File: backend/routers/siswa.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/siswa",
    tags=["Siswa"]
)

@router.get("/", response_model=List[schemas.SiswaResponse])
def get_all_siswa(db: Session = Depends(get_db)):
    return db.query(models.Siswa).all()

@router.post("/", response_model=schemas.SiswaResponse)
def create_siswa(siswa: schemas.SiswaCreate, db: Session = Depends(get_db)):
    db_siswa = models.Siswa(nama=siswa.nama, kelas=siswa.kelas)
    db.add(db_siswa)
    db.commit()
    db.refresh(db_siswa)
    return db_siswa

@router.put("/{siswa_id}", response_model=schemas.SiswaResponse)
def update_siswa(siswa_id: int, siswa: schemas.SiswaCreate, db: Session = Depends(get_db)):
    db_siswa = db.query(models.Siswa).filter(models.Siswa.id == siswa_id).first()
    if not db_siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    
    db_siswa.nama = siswa.nama
    db_siswa.kelas = siswa.kelas
    db.commit()
    db.refresh(db_siswa)
    return db_siswa

@router.delete("/{siswa_id}")
def delete_siswa(siswa_id: int, db: Session = Depends(get_db)):
    db_siswa = db.query(models.Siswa).filter(models.Siswa.id == siswa_id).first()
    if not db_siswa:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    
    db.delete(db_siswa)
    db.commit()
    return {"message": "Data siswa berhasil dihapus"}
