from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from auth import create_token, decode_token, revoke_token, revoked_tokens
from models import verify_login

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@router.post("/login")
async def login(credentials: OAuth2PasswordRequestForm = Depends()):
    # validate username and password
    if not verify_login(credentials.username, credentials.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    # generate access token
    user_info = {
        "user": credentials.username,
    }
    token = create_token(user_info, expires_delta=timedelta(minutes=15))
    return {"token": token}


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    decoded_token = decode_token(token)
    if decoded_token is None:
        raise HTTPException(status_code=401, detail="Invalid Token")

    revoke_token(token)
    return {"logged_out": True}


@router.get("/secret")
def secret(token: str = Depends(oauth2_scheme)):
    decoded_token = decode_token(token)
    if decoded_token is None or token in revoked_tokens:
        raise HTTPException(status_code=401, detail="Invalid Token")
    with open("decoded_store.txt", "r") as f:
        secret_data = f.read()
    return {"verified": True,
            "user_info": decoded_token.get("user"),
            "secret_data": secret_data}
