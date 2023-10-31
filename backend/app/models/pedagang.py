from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app import db
from app.models.dataType import Data_Type, Relations

Base = declarative_base()


class Data_pedagang(db.Model, Base):
    __tablename__ = 'data_pedagang'

    id_pedagang = Data_Type.id()
    nama_pedagang = Data_Type.string()
    alamat_pedagang = Data_Type.string()
    created_at = Data_Type.time_now()
    delete_at = Data_Type.time_now()
    
    # relationship
    id_dagangan = Relations.relation('data_dagangan', 'data_pedagang')
    id_setoran = Relations.relation('data_setoran', 'data_pedagang')


class Data_dagangan(db.Model, Base):
    __tablename__ = 'data_dagangan'

    id_dagangan = Data_Type.id()
    banyak_dagangan = Data_Type.integer()
    created_at = Data_Type.time_now()

    # foreignkey
    id_pedagang = Relations.foreign_key('data_pedagang.id_pedagang')


class Data_setoran(db.Model, Base):
    __tablename__ = 'data_setoran'

    id_setoran = Data_Type.id()
    jumlah_setoran = Data_Type.integer()
    created_at = Data_Type.time_now()

    # foreignkey
    id_pedagang = Relations.foreign_key('data_pedagang.id_pedagang')


# ade farhan is on game