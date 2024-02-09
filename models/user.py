from typing import List
from pydantic import BaseModel


# class ReqruiterSkills(BaseModel):
#     department_names: str
#     skill: List[str]

class Department(BaseModel):
    name: str
    department_name: str
    tenure: int
    skills: List[str]
