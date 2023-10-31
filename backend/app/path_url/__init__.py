from app import api
from app.controllers.c_pedagang import PedagangResource

def pedagang_api_path():
    api.add_resource(PedagangResource, "/api")