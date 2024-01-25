from pydantic import BaseModel, EmailStr, constr


class RegistrationUserSchema(BaseModel):
    name: str 
    email: EmailStr
    group: str
    password: constr(min_length=8)
    password_confirm: str
    role: str


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class ResponseUser(BaseModel):
    status: str
