from .router import router
from fastapi import HTTPException
from auth.jtw_handler import criar_token
from decouple import config


# Login para gerar TOKEN
user = config('USER_JWT')
password = config('PASSWORD_JWT')
print(user)


@router.post("/login")
def login(usuario: str, senha: str):
    if usuario == user and senha == password:
        token = criar_token({"sub": usuario})
        return {"access_token": token}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
