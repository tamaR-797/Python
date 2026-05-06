from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, constr
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Task(BaseModel):
    name: str
    description: str
    id: str = Field(default_factory=lambda: str(uuid4()))
    status: str = Field(..., regex='^(open|closed)$')

tasks_db = []

@app.post("/tasks/")
def create_task(task: Task):
    tasks_db.append(task)
    return task

@app.get("/tasks/")
def read_tasks():
    return tasks_db

@app.get("/tasks/{task_id}")
def read_task(task_id: str):
    task = next((task for task in tasks_db if task.id == task_id))
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    task_index = next((index for index, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_index] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    task_index = next((index for index, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db.pop(task_index)