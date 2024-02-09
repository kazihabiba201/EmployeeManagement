def employeeEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
         "department": item["department_name"], 
        "tenure": item["tenure"],
        "skills":  item["skills"]
    }

def employeesEntity(entity) -> list:
    return [employeeEntity(item) for item in entity]