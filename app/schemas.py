from typing import Optional
from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

class Student(StudentBase):
    id: str

    class Config:
        orm_mode = True
