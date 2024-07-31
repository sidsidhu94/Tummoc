from sqlalchemy.orm import Session
from fastapi import HTTPException
import models
import schemas

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(name=teacher.name, subject=teacher.subject)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()




def update_teacher(db: Session, teacher_id: int, teacher: schemas.TeacherCreate):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher:
        db_teacher.name = teacher.name
        db_teacher.subject = teacher.subject
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return {"detail": "Teacher deleted"}

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, standard=student.standard)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
    



def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()



def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db_student.name = student.name
        db_student.standard = student.standard
        db_student.teacher_id = student.teacher_id
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return {"detail": "Student deleted"}

def assign_student(db: Session, student_id: int, teacher_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db_student.teacher_id = teacher_id
        db.commit()
        db.refresh(db_student)
    return {"detail": "Student assigned to teacher"}

