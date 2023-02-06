from fastapi import FastAPI, HTTPException, Body
from datetime import date
from pymongo import MongoClient
from pydantic import BaseModel

DATABASE_NAME = "hotel"
COLLECTION_NAME = "reservation"
MONGODB_URL = "mongodb://localhost"
MONGODB_PORT = 27017


class Reservation(BaseModel):
    name : str
    start_date: date
    end_date: date
    room_id: int


client = MongoClient(MONGODB_URL, MONGODB_PORT)

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]

app = FastAPI()


@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    pass

@app.get("/reservation/by-room/{room_id}")
def get_reservation_by_room(room_id: int):
    pass

@app.post("/reservation")
def reserve(reservation : Reservation):
    pass

@app.put("/reservation/update")
def update_reservation(reservation: Reservation, new_start_date: date = Body(), new_end_date: date = Body()):
    pass

@app.delete("/reservation/delete")
def cancel_reservation(reservation: Reservation):
    pass