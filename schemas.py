from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    standard: str
    # teacher_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    # teacher: Optional[int] = None  
    teacher_id: Optional[int]
    class Config:
        orm_mode = True
        from_attributes = True

class TeacherBase(BaseModel):
    name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    students: List[int] = []  
    class Config:
        orm_mode = True
        from_attributes = True

class AssignStudentRequest(BaseModel):
    student_id: int
    teacher_id: int

class ResponseMessage(BaseModel):
    detail: str


