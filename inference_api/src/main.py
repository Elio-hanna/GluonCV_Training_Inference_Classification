from fastapi import FastAPI
from api.controllers import fetch_model_controller,image_classification_controller

app = FastAPI()

app.include_router(
    fetch_model_controller.router,
    prefix="/fetch_module",
    tags=["fetch_module"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    image_classification_controller.router,
    prefix="/inference_module",
    tags=["classification_module"],
    responses={404: {"description": "Not found"}},
)