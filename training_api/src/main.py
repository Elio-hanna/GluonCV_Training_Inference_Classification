from fastapi import FastAPI

# from api.controllers import training_with_name_controller

from api.controllers import training_model_controller,training_with_name_controller
app = FastAPI()

app.include_router(
    training_model_controller.router,
    prefix="/training_module",
    tags=["training_json"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    training_with_name_controller.router,
    prefix="/training_module",
    tags=["training_default"],
    responses={404: {"description": "Not found"}},
)