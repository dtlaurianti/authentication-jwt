from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from auth import create_token, decode_token, revoke_token, revoked_tokens
from models import verify_login, register_user

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/register")
async def register(form: OAuth2PasswordRequestForm = Depends()):
    if not register_user(form.username, form.password):
        raise HTTPException(status_code=400, detail="User already exists")
    return {"registered": True}

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # validate username and password
    if not verify_login(form.username, form.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    # generate access token
    user_info = {
        "user": form.username,
        "scope": "read"
    }
    token = create_token(user_info, expires_delta=timedelta(minutes=15))
    return {"access_token": token}

@router.post("/logout")
def logout(token: str = Depends(oauth2)):
    decoded_token = decode_token(token)
    if decoded_token is None:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    revoke_token(token)
    return {"logged_out": True}

@router.get("/secret")
def secret(token: str = Depends(oauth2)):
    decoded_token = decode_token(token)
    if decoded_token is None or decoded_token in revoked_tokens:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    return {"verified" : True, "user_info": decoded_token.get("user")}