from pydantic import BaseModel, EmailStr
from enum import Enum


class Roles(str, Enum):
    teacher = "teacher"
    student = "student"
    admin = "admin"


class RolesModel(BaseModel):
    username: str
    password: str
    role: Roles

class UserModel(BaseModel):
    username:str
    role:Roles
class StudentModel(BaseModel):
    name: str = ""
    roll_no: int
    Math_marks: int = 0
    Science_marks: int = 0
    Hindi_marks: int = 0
    English_marks: int = 0
    Total_marks: int = 0
    Rank: int = -1
    Teacher_id: int | None = None

    class Config:
        orm_mode = True


class TeacherModel(BaseModel):
    teacher_name: str
    mobile_no: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
