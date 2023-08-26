from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Form, HTTPException, Depends
from starlette import status
from Databases.models import Student, Teacher, User
from Databases.session import get_db
from Databases.schema import StudentModel, TeacherModel, RolesModel, Roles, UserModel
from fastapi import APIRouter
import jwt
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from security.auth import (
    hash_password, verify_password, generate_token
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

path = APIRouter()


@path.post("/token")
async def generate(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = form.username
    plain_password = form.password

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    detail = db.query(User).filter(User.username == username).first()
    if detail is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if verify_password(plain_password, detail.password) is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = generate_token(UserModel(**detail.__dict__))
    return {"access_token": token, "token_type": "bearer"}


def verify_token(token: str = Depends(oauth2_scheme), secret_key="secret", algo="HS256"):
    if token:
        payload = jwt.decode(token, secret_key, algorithms=[algo])
        return payload
    else:
        return {"message": "token missing"}


@path.delete("/tec_del")
async def del_teachers(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )

    details = db.query(Teacher).delete()
    db.commit()
    return {"model": details}


@path.get("/teachers")
async def get_teachers(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    details = db.query(Teacher).all()
    return {"model": details}


@path.get("/teachers/{teacher_id}")
async def get_teachers(teacher_id: int, student_name: str | None = None, student_roll: int | None = None,
                       payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role == "student":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    teacher = db.query(Teacher).get(teacher_id)
    if teacher is None:
        return {"message": "Teacher id is not valid"}

    if student_roll is not None:
        details = db.query(Student).filter_by(Teacher_id=teacher_id, roll_no=student_roll).all()
        return {"message": details}

    if student_name is not None:
        details = db.query(Student).filter_by(Teacher_id=teacher_id, name=student_name).all()
        return {"model": details}
    return {"model": teacher}


@path.get("/teachers/{id}/student")
async def get_teachers(id: int, db: Session = Depends(get_db)):
    details = db.query(Student).filter_by(Teacher_id=id).all()
    return {"model": details}


## Only access by admin
@path.get("/admin")
async def get_admin(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    details = db.query(User).filter_by(role="admin").all()
    return {"details": details}


## Only accessed by admin
@path.get("/users")
async def get_user(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    users_details = db.query(User).all()
    return {"message": users_details}


@path.post("/admin")
async def add_user(Username: str, password: str,payload: dict = Depends(verify_token) ,db: Session = Depends(get_db)):
    role = payload["role"]
    time = payload["expire_time"]
    if datetime.fromtimestamp(time) <= datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if payload["username"] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only access by admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    admin_user = User(username=Username, password=hash_password(password), role=Roles.admin)
    db.add(admin_user)
    db.commit()

    return {"message": "User added successfully as admin"}


@path.delete("/del_user")
async def del_Users(db: Session = Depends(get_db)):
    details = db.query(User).delete()
    db.commit()
    return {"model": details}


@path.post("/teacher")
async def post_teach(teacher: TeacherModel, db: Session = Depends(get_db)):
    ty = Teacher(**teacher.model_dump())
    db.add(ty)
    db.commit()
    user = User(username=teacher.teacher_name.replace(" ", ""),
                password=hash_password(teacher.password),
                role=Roles.teacher)
    db.add(user)
    db.commit()
    return {"message": "Teacher Data Added Successfully"}


# This api delete all the student from table
@path.delete("/del_student")
async def del_students(db: Session = Depends(get_db)):
    details = db.query(Student).delete()
    db.commit()
    return {"model": details}


# Get all student details
@path.get("/Student")
async def get_students(db: Session = Depends(get_db)):
    details = db.query(Student).all()
    return {"model": details}


@path.post("teacher/{id}/student")
async def post_teach(student: StudentModel, teacher_id: int, db: Session = Depends(get_db)):
    ty = Student(**student.model_dump())
    db.add(ty)
    db.commit()

    return {"message": "Student added successfully"}

# @path.get("/teacher/{id}/student")
# async def get_all_student(id:int, db: Session = Depends(get_db)):
#     entries=db.query(Student).filter(Teacher_id=id)
#     return {"Entries":entries}
#
# @path.get("student/{id}")
# async def get_student(id:int, db: Session = Depends(get_db)):
#     entries=db.query(Student).get(id)
#     return {"Entries":entries}
