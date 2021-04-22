from fastapi import APIRouter, HTTPException
from application.fetch_model.services.fetch_model_service import FetchModelService

router = APIRouter()


@router.get("/models")
async def list_models():
    """
    Lists all available models
    :return: names
    """
    try:
        return FetchModelService().fetch_all_models()
    except Exception:
        raise HTTPException(status_code=300, detail="cannot list all the models")
