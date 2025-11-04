from fastapi import FastAPI
from app.routes import employees, departments
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System")

app.include_router(departments.router)
app.include_router(employees.router)
