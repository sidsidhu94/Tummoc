from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String, index=True)
    students = relationship("Student", back_populates="teacher")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    standard = Column(String, index=True)  
    teacher_id = Column(Integer, ForeignKey("teachers.id"),nullable=True)

    teacher = relationship("Teacher", back_populates="students")