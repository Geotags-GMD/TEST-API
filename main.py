# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/region-v")
async  def root():
    return {"message": "REGION V"}

@app.get("/region-x")
async  def root():
    return {"message": "REGION X"}