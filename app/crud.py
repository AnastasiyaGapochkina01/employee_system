from sqlalchemy.orm import Session
from . import models, schemas

def get_departments(db: Session):
    return db.query(models.Department).all()

def create_department(db: Session, dept: schemas.DepartmentCreate):
    new = models.Department(**dept.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def get_employees(db: Session):
    return db.query(models.Employee).all()

def create_employee(db: Session, emp: schemas.EmployeeCreate):
    new = models.Employee(**emp.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new
