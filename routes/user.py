from fastapi import APIRouter
from models.user import Department 
from config.db import conn 
from schemas.user import employeeEntity, employeesEntity
from bson import ObjectId

user = APIRouter() 

@user.get('/')
async def find_all_employees():
    print(conn.local.user.find())
    print(employeesEntity(conn.local.user.find()))
    return employeesEntity(conn.local.user.find())



@user.get('/{id}')
async def find_one_employee(id):
    return employeeEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_employees(user: Department):
    conn.local.user.insert_one(dict(user))
    return employeesEntity(conn.local.user.find())


@user.put('/{id}')
async def update_employee(id,user: Department):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return employeeEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_employee(id,user: Department):
    return employeeEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))