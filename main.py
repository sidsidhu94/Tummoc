from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import schemas
import models
import crud
from schemas import AssignStudentRequest
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, teacher=teacher)

@app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    
    return {
        "id": teacher.id,
        "name": teacher.name,
        "subject": teacher.subject,
        "students": [student.id for student in teacher.students]
    }

@app.put("/teachers/{teacher_id}", response_model=schemas.Teacher)
def update_teacher(teacher_id: int, teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    updated_teacher = crud.update_teacher(db, teacher_id=teacher_id, teacher=teacher)
    if updated_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated_teacher



@app.delete("/teachers/{teacher_id}", response_model=dict)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    result = crud.delete_teacher(db, teacher_id=teacher_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"detail": "Teacher deleted"}

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student=student)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id=student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id=student_id, student=student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.delete("/students/{student_id}", response_model=dict)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    result = crud.delete_student(db, student_id=student_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted"}



@app.post("/assign_student/", response_model=dict)
def assign_student(request: AssignStudentRequest, db: Session = Depends(get_db)):
    result = crud.assign_student(db, student_id=request.student_id, teacher_id=request.teacher_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student or Teacher not found")
    return {"detail":"Student assigned to teacher"}
