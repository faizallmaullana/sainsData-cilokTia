from flask import jsonify, request
from flask_restful import Resource
from app.models.pedagang import *


class SetoranResource(Resource):
    def post(self):
        #####
        id_pedagang = request.json.get('id_pedagang')
        jumlah_setoran = request.json.get('jumlah_setoran', 0)
        #####

        if jumlah_setoran <= 0:
            return {
                "msg": "Jumlah setoran harus disi dengan benar",
                "status_code": "400"
            }, 400

        value = Data_setoran(
            id_pedagang=id_pedagang,
            jumlah_setoran=jumlah_setoran
        )

        db.session.add(value)
        db.session.commit()

        return {
            "msg": "created",
            "status_code": 201,
            "data": {
                "id_setoran": value.id_setoran
        }}, 201

        
    def put(self, id_setoran):
        data = Data_setoran.query.filter_by(id_setoran=id_setoran).first()

        #####
        jumlah_setoran = request.json.get("jumlah_setoran", data.jumlah_setoran)
        #####

        data.jumlah_setoran = jumlah_setoran
        db.session.commit()

        return {
            "msg": "updated",
            "status_code": 201,
            "data": {
                "id_setoran": data.id_setoran
            }
        }, 201


    def delete(self, id_setoran):
        data = Data_setoran.query.filter_by(id_setoran=id_setoran).first()

        db.session.delete(data)
        db.session.commit()

        return {
            "msg": "deleted",
            "status_code": 201
        }, 201


class SisaSetoranResource(Resource):
    def get(self, id_pedagang):
        pedagang = Data_pedagang.query.filter_by(id_pedagang=id_pedagang).first()
        dagangan = Data_dagangan.query.filter_by(id_pedagang=id_pedagang).all()
        setoran = Data_setoran.query.filter_by(id_pedagang=id_pedagang).all()

        banyak_dagangan = 0
        total_setoran = 0

        for data in dagangan:
            banyak_dagangan += int(data.banyak_dagangan)
        
        for data in setoran:
            total_setoran += int(data.jumlah_setoran)

        harus_disetorkan = int(banyak_dagangan) * 350

        sisa_setoran = harus_disetorkan - total_setoran

        return {
            "msg": "ok",
            "status_code": 200,
            "data": {
                "id_pedagang": id_pedagang,
                "nama_pedagang": pedagang.nama_pedagang,
                "Sisa_setoran": sisa_setoran
            }
        }, 200