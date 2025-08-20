from fastapi import FastAPI
import uvicorn
from  dal_mongo import DAL_mongo
from solider import Solider
import os

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD", None)
DB = os.getenv("DATABASE", "enemy_soldiers")
COLLECTION = os.getenv("COLLECTION", "soldier_details")


app = FastAPI()
dal = DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)


@app.get("/")
async def status():
    connection = dal.open_connection()
    if connection:
        return {"status: ": "ok"}
    else:
        return {"status: ": "fail to connect"}


@app.get("/get_data")
async def get_data():
    connect = dal.open_connection()
    if connect:
        try:
            data= dal.get_all()
            return {"result ": data}
        except Exception as e:
            print("error : ", e)
        finally:
            dal.close_connection()
    else:
        return {"status: ": "fail to connect"}


@app.post("/post_data")
async def post_data( solider: Solider):
    connect = dal.open_connection()
    if connect:
        try:
            data= {"id": solider.id, "first_name": solider.first_name,"last_name": solider.last_name,
                   "phone_number": solider.phone_number, "rank":solider.rank}
            result = dal.insert_one(data)
            return {"status ": "ok"}
        except Exception as e:
            print("error : ", e)
        finally:
            dal.close_connection()
    else:
        return {"status: ": "fail to connect"}


@app.put("/update")
async def update_solider(id, field, new_value):
    connect = dal.open_connection()
    if connect:
        try:
            result = dal.update_one(int(id), field, new_value)
            return {"status ": "ok"}
        except Exception as e:
            print("error : ", e)
        finally:
            dal.close_connection()
    else:
        return {"status: ": "fail to connect"}


@app.delete("/delete")
async def delete_solider(id):
    connect = dal.open_connection()
    if connect:
        try:
            result = dal.delete_one(int(id))
            return {"status ": "ok"}
        except Exception as e:
            print("error : ", e)
        finally:
            dal.close_connection()
    else:
        return {"status: ": "fail to connect"}




if __name__ == "__main__":
    uvicorn.run(app , host="0.0.0.0", port=8080)
