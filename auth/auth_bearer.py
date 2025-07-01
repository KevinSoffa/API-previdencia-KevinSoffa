from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, HTTPException
from .jtw_handler import verificar_token  


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            token = credentials.credentials
            if verificar_token(token) is None:
                raise HTTPException(status_code=403, detail="Token inválido ou expirado.")
            return token
        else:
            raise HTTPException(status_code=403, detail="Token ausente.")
