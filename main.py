from fastapi import FastAPI , APIRouter

app = FastAPI()

version_v1 = APIRouter()
version_v2 = APIRouter()

@version_v1.get("/tasks/" ,description= "Get all tasks")
async def get_tasks_v1():
    return {"message": "get tasks for version 1"}
    

@version_v2.get("/tasks/")
async def get_tasks_v2():
    return {"message": "get tasks for version 2"}

@version_v1.get("/items/" , description= "Get all tasks")
async def get_items_v1():
    return {"message": "get tasks for version 1"}
    

@version_v2.get("/items/")
async def get_items_v2():
    return {"message": "get tasks for version 2"}

#include the routers with version prfixes

app.include_router(version_v1, prefix = '/v1', tags=["Version 1 API's"], )
app.include_router(version_v2 , prefix = '/v2', tags=["Version 2 API's"])