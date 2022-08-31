from pydantic import BaseModel


class sh_demo(BaseModel):
    time: int
    speed:int
    mode :int
