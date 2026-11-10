from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class student(BaseModel):
    id:int
    name:str
    marks:float
students={}

@app.post("/students")
def add (s:student):
    if s.id in students:
        raise HTTPException(400,"student already exists")
    students[s.id]=s
    return s

@app.get("/students")
def get():
    return students

@app.get("/students/{id}")
def getone(id:int):
    if id not in students:
        raise HTTPException(404,"student doesnt exist")
    return students[id]

@app.put("/students/{id}")
def update(id:int,s:student):
    if id not in students:
        raise HTTPException(404,"student doesnt exist")
    if s.id!=id:
        raise HTTPException(404,"student ID Mismatch")
    students[id]=s
    return s

@app.delete("/students/{id}")
def delete(id:int):
    if id not in students:
        raise HTTPException(404,"student doesnt exist")
    del students[id]
    return {"message":"data deleted"}