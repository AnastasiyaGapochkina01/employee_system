# Employeer management system
Простое CRUD‑приложение для учета сотрудников и отделов. 

## Запросы (для проверок)
Добавить отдел
```bash
curl -X POST http://localhost:8000/departments/ -H "Content-Type: application/json" -d '{"name": "IT Department"}'
```
Получить список отделов
```bash
curl http://localhost:8000/departments/
```
Добавить сотрудника
```bash
curl -X POST http://localhost:8000/employees/ -H "Content-Type: application/json" -d '{ "name": "Petrov I", "position": "DevOps", "email": "ivan.petrov@example.com", "phone": "+79991234567", "hire_date": "2024-09-01", "salary": 150000, "department_id": 1 }'
```
Получить список сотрудников
```bash
curl http://localhost:8000/employees/
```
