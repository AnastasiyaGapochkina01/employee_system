from pydantic import BaseModel, EmailStr, Field
from datetime import date

class DepartmentBase(BaseModel):
    name: str = Field(..., min_length=2)

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=2)
    position: str
    email: EmailStr
    phone: str = Field(..., min_length=10)
    hire_date: date
    salary: float = Field(..., gt=0)
    department_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    department: Department
    class Config:
        orm_mode = True
