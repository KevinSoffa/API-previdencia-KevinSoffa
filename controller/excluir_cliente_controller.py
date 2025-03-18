from service.excluir_cliente_service import excluir_cliente_service
from fastapi import HTTPException
from .router import router


@router.delete("/excluir/cliente/{id_cliente}", response_model=dict)
async def excluir_cliente_controller(id_cliente: str):
    try:
        resultado = excluir_cliente_service(id_cliente)

        if not resultado["success"]:
            raise HTTPException(status_code=404, detail=resultado["message"])
        
        return {
            "message": resultado["message"],
            "planos_excluidos": resultado["planos_excluidos"]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
