from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from Databases.schema import Roles
from Databases.session import Base, engine


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    roll_no = Column(Integer)
    Math_marks = Column(Integer)
    Science_marks = Column(Integer)
    Hindi_marks = Column(Integer)
    English_marks = Column(Integer)
    Total_marks = Column(Integer)
    Rank = Column(Integer)
    Teacher_id = Column(Integer, ForeignKey("teacher.id"))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(Roles))


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String)
    mobile_no = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


Base.metadata.create_all(bind=engine)
