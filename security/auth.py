import bcrypt
# from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
# from sqlalchemy.orm import Session
import jwt
# from fastapi import Depends
# from Databases.models import Teacher,Student
# from Databases.session import get_db
from Databases.schema import UserModel
# from fastapi import HTTPException,Security
# from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from datetime import datetime,timedelta
# from pydantic import BaseModel

# oauth_scheme=OAuth2PasswordBearer(tokenUrl="/token")



def hash_password(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# fake_users_db = {
#     "testuser": {
#         "username": "testuser",
#         "password": "testpassword"
#     }
# }
# class User(BaseModel):
#     username: str
#
# def is_teacher(username:str,password:str,db:Session= Depends(get_db)):
#     if username  is None or password is None:
#         return False
#     detail=db.query(Teacher).filter()
#
#     ...
# def is_student(username:str,password:str,db:Session= Depends(get_db)):
#     if username  is None or password is None:
#         return False
# def is_admin(username:str,password:str,db:Session= Depends(get_db)):
#     if username  is None or password is None:
#         return False
# # secret:str="secret", db: Session=Depends(get_db)
# def authenticate_user(account:RolesModel):
#
#     role=account["role"]
#     if role=="student":
#         verified=is_student()
#         if verified is False:
#             return "Credetionals are wrong"
#         ...
#     elif role=="teacher":
#         verified=is_teacher()
#         if verified is False:
#             return "Credetionals are wrong"
#         ...
#     else:
#         verified=is_admin()
#         if verified is False:
#             return "Credetionals are wrong"
#         ...
def generate_token(account:UserModel,key:str="secret"):
    expiration = datetime.utcnow() + timedelta(minutes=30)
    payload=account.model_dump()
    payload["expire_time"]=expiration.timestamp()

    token=jwt.encode(payload,key,algorithm="HS256")
    return token

def decode_token(token:str,key:str="secret"):
    payload=jwt.decode(token,key,algorithms="HS256")
    return payload

#
# #user= {"username":"alpha_123","password":"Alpha@123","role":"student"}
# user = RolesModel(username="alpha_123", password="Alpha@123", role="student")
# '''
#
# for genertaing token we want verifed user name password and payload
#
# '''
#
#
# #print(generate_token(user))
# # token=jwt.encode(user,key="secret")
# # print(token)
# # payload=jwt.decode(token,algorithms="HS256",key="secret")
# # print(payload["role"])