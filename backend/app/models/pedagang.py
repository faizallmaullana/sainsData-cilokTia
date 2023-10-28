from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app import db
from app.models.dataType import Data_Type

Base = declarative_base()


class Data_pedagang(db.Model, Base):
    __tablename__ = 'data_pedagang'

    id_pedagang = Data_Type.id()
    nama_pedagang = Data_Type.string()
    alamat_pedagang = Data_Type.string()

    created_at = Data_Type.time_now()
    delete_at = Data_Type.time_now()


class Data_dagangan(db.Model, Base):
    __tablename__ = 'data_dagangan'

    id_dagangan = Data_Type.id()
    banyak_dagangan = Data_Type.integer()
    
    created_at = Data_Type.time_now()
    