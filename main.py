from fastapi import FastAPI
from router import view

app=FastAPI()

app.include_router(view.path)

# @app.get("/")
# async def get():
#     return {"message":"success"}