from fastapi import Depends, HTTPException, status, Request
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
import jwt, os
from app.config import API_KEY, AUTH_TYPE

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

def get_jwt_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No JWT token found")
    token = auth_header.split(" ")[1]
    try:
        jwt.decode(token, os.getenv("JWT_SECRET", "jwtsecret"), algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid JWT")
        
def get_auth(request: Request, api_key: str = Depends(api_key_header), token: str = Depends(oauth2_scheme)):
    if AUTH_TYPE == "api_key":
        return get_api_key(api_key)
    elif AUTH_TYPE == "jwt":
        return get_jwt_token(request)
    elif AUTH_TYPE == "oauth2":
        if not token:
            raise HTTPException(status_code=401, detail="No OAuth2 token found")
        # add your custom OAuth2 validation here
    else:
        raise HTTPException(status_code=401, detail="Unknown authentication type")
