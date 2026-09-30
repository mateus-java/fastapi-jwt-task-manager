from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from datetime import timedelta
from typing import List
from database import create_db_and_tables, get_session
from models import User, Task
from auth import (
    get_password_hash,
    authenticate_user,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

app = FastAPI(title="API de Tarefas com JWT", version="1.0")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register", response_model=dict)
def register(user_data: dict, session: Session = Depends(get_session)):
    username = user_data.get("username")
    password = user_data.get("password")
    
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username e password são obrigatórios")
    
    existing_user = session.exec(select(User).where(User.username == username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    
    hashed_pw = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_pw)
    session.add(new_user)
    session.commit()
    return {"message": "Usuário criado com sucesso!"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks/", response_model=Task)
def create_task(title: str, description: str = None, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    task = Task(title=title, description=description, owner_id=current_user.id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.get("/tasks/", response_model=List[Task])
def get_tasks(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(Task).where(Task.owner_id == current_user.id)
    tasks = session.exec(statement).all()
    return tasks