from flask import jsonify, request
from flask_restful import Resource
from app.models.pedagang import *

class DaganganResource(Resource):
    def post(self):
        #####
        id_pedagang = request.json.get('id_pedagang')
        banyak_dagangan = request.json.get('banyak_dagangan', 0)
        #####

        if banyak_dagangan <= 0:
            return {
                "msg": "Silahkan isi banyak dagangan",
                "status_code": 400
            }, 400
        
        value = Data_dagangan(
            id_pedagang=id_pedagang,
            banyak_dagangan=banyak_dagangan
        )

        db.session.add(value)
        db.session.commit()
        
        return {
            "msg": "created",
            "status_code": 201,
        }, 201


    # get data dagangan based on pedagang
    def get(self, id_pedagang):
        datas = Data_dagangan.query.filter_by(id_pedagang=id_pedagang).all()
        data_pedagang = Data_pedagang.query.filter_by(id_pedagang=id_pedagang).first()
        nama_pedagang = data_pedagang.nama_pedagang
        result = []
        
        # jika data kosong
        if datas == []:
            return {
                "msg": "Data masih kosong",
                "status_code": 200
            }, 200

        for data in datas:
            result.append({
                "id_pedagang": id_pedagang,
                "id_dagangan": data.id_dagangan,
                "nama_pedagang": nama_pedagang,
                "banyak_dagangan": data.banyak_dagangan
            })

        return {
            "msg": "ok",
            "status_code": 200,
            "data": result
        }, 200

    