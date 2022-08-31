from importlib.resources import path
from fastapi import APIRouter
from schemas.schemas import sh_demo
import json

api =APIRouter()



@api.get("/param/select")
async def ddd():
    path="./file/data.json"
    f=open(path, 'r')
    data = json.load(f)
    content = f.read()
    return data 


@api.post("/param/param_update")
def param_update(d:sh_demo):
    with open("./file/data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["time"] = d.time
    data["speed"] = d.speed
    data["mode_fonctionnement"] = d.mode
    with open("./file/data.json", "w") as jsonFile:
       json.dump(data, jsonFile)

 