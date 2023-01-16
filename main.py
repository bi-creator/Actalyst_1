from fastapi import FastAPI,Response, status
from fastapi.middleware.cors import CORSMiddleware
from query import executeQuery
from datetime import datetime,timedelta
import pytz
from pydantic import BaseModel
class dataToStream(BaseModel):
    column_1: str
    column_2:str
    column_3:str
    column_4:str
    column_5:str


IST = pytz.timezone('Asia/Kolkata')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.post('/streamData')
def addCourts(dataToStream:dataToStream):
    data=executeQuery("INSERT INTO test_table_1 (column_1, column_2, column_3,column_4,column_5) VALUES (%s,%s,%s,%s,%s)" ,[dataToStream.column_1,dataToStream.column_2,dataToStream.column_3,dataToStream.column_4,dataToStream.column_5])
    return data


@app.get('/getData')
def getData():
    data=executeQuery('SELECT * from public.test_table_1')
    return data
