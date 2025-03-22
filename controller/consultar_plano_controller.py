from service.consultar_plano_service import consultar_plano_service
from fastapi import HTTPException
from .router import router

@router.get("/consultar/plano/{id_plano}")
def consultar_plano_controller(id_plano: str):
    try:
        plano = consultar_plano_service(id_plano)
        return {"plano": plano}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Erro interno no servidor.{e}")