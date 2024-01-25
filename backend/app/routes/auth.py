from fastapi import APIRouter



router = APIRouter()



users=[]

@router.post('/register', response_model=_user.ResponseUser)
async def login_user(user: _user.RegistrationUserSchema) -> _user.RegistrationUserSchema:
    users.append(user)
    status = _user.ResponseUser(status='good')
    return status