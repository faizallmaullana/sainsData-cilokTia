from flask import jsonify, request
from flask_restful import Resource
from app.models.pedagang import Data_pedagang
from app import db

class PedagangResource(Resource):
    def post(self):
        #####
        nama_pedagang = request.json.get('nama_pedagang', None)
        alamat_pedagang = request.json.get('alamat_pedagang', None)
        #####

        value = Data_pedagang(
            nama_pedagang=nama_pedagang,
            alamat_pedagang=alamat_pedagang,
            )

        db.session.add(value)
        db.session.commit()

        return {
            "msg": "created",
            "status_code": 201
        }, 201

    def get(self):
        datas = Data_pedagang.query.all()
        result = []

        for data in datas:
            result.append({
                "id_pedagang": data.id_pedagang,
                "nama_pedagang": data.nama_pedagang,
                "alamat_pedagang": data.alamat_pedagang,
                "created_at": data.created_at.strftime("%d-%m-%Y")
            })

        return {
            "msg": "ok",
            "status_code": 200,
            "data": result
        }, 200


    def put(self, id_pedagang):
        data = Data_pedagang.query.filter_by(id_pedagang=id_pedagang).first()\

        #####
        nama_pedagang = request.json.get("nama_pedagang", data.nama_pedagang)
        alamat_pedagang = request.json.get("alamat_pedagang", data.alamat_pedagang)
        #####

        data.nama_pedagang = nama_pedagang
        data.alamat_pedagang = alamat_pedagang
        db.session.commit()

        return {
            "msg": "changed",
            "status_code": 201,
            "data": {
                id_pedagang: data.id_pedagang
            }
        }, 200


    def delete(self, id_pedagang):
        data = Data_pedagang.query.filter_by(id_pedagang=id_pedagang).first()

        db.session.delete(data)
        db.session.commit()

        return {
            "msg": "deleted",
            "status_code": 204
        }, 204