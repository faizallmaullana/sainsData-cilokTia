from app import api
from app.controllers.c_pedagang import PedagangResource
from app.controllers.c_dagangan import DaganganResource

def pedagang_api_path():
    # Pedagang
    api.add_resource(PedagangResource, "/api/pedagang")
    api.add_resource(PedagangResource, "/api/pedagang/<string:id_pedagang>", endpoint="PedagangResource.put", methods=["PUT"])
    api.add_resource(PedagangResource, "/api/pedagang/<string:id_pedagang>", endpoint="PedagangResource.delete", methods=["DELETE"])

    # Dagangan
    api.add_resource(DaganganResource, "/api/dagangan")
    api.add_resource(DaganganResource, "/api/dagangan/<string:id_pedagang>", endpoint="DaganganResource.get", methods=["GET"])
    api.add_resource(DaganganResource, "/api/dagangan/<string:id_dagangan>", endpoint="DaganganResource.put", methods=["PUT"])
    api.add_resource(DaganganResource, "/api/dagangan/<string:id_dagangan>", endpoint="DaganganResource.delete", methods=["Delete"])

    # Setoran