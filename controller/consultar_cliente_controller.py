from service.consultar_cliente_service import consultar_cliente_service
from fastapi import HTTPException, status
from .router import router


@router.get("/consultar/cliente/{id_cliente}")
def consultar_cliente_controller(id_cliente: str):
    try:
        cliente = consultar_cliente_service(id_cliente)
        return {"cliente": cliente}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Erro interno no servidor.{e}")