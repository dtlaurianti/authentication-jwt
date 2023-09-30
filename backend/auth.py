import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta

SECRET_KEY = "secret"
ALGORITHM = "HS256"

# tokens are revoked on logout
revoked_tokens = set()

def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except PyJWTError:
        return None

    return decoded_token

def revoke_token(token: str):
    revoked_tokens.add(token)