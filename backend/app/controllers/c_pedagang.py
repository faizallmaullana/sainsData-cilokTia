from flask import jsonify, request
from flask_restful import Resource
from app.models.pedagang import *

class PedagangResource(Resource):
    def get(self):
        print(0)
        datas = Data_pedagang.query.All()
        result = []
        for data in datas:
            result.append({
                "id_pedagang": data.id_pedagang,
                "nama_pedagang": data.nama_pedagang,
                "alamat_pedagang": data.alamat_pedagang,
                "created_at": data.created_at
            })
        return 0

    def post(self):
        nama = request.json.get('nama', None)
        value = Data_pedagang(
            nama_pedagang=nama, is_deleted=0)
        db.session.add(value)
        db.session.commit()
        return 0