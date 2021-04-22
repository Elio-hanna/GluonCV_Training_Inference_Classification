from application.training_module import train_model
from fastapi import APIRouter,HTTPException
from application.logging.services import logging_service
from DTO.parameter_information import ParameterInformation

router = APIRouter()
logging = logging_service.LoggingService()

@router.post("/train_model/")
async def create_model(item: ParameterInformation):
    """
    the user submit a json object that contain all the details needed to create and train a model
    :param item:
    :return:
    """
    Model = train_model.TrainModel()
    parr = "learning rate: " + str(item.learning_rate) + " batch: " + str(item.batch) + " epochs: " + str(item.epchs) + " "
    try:
        print("here")
        Model.create_and_train(model_name=item.name, batch_size=item.batch, learning_rate=item.learning_rate, epochs=item.epchs)
        # Model.create_and_train(item)
        logging.log(name=create_model.__name__, result="ModelCreationService saved " + item.name, parm=parr)
        return {"ModelCreationService Trained and saved in": item.name}
    except Exception as ex:
        logging.log_error(create_model.__name__)
        raise HTTPException(status_code=404, detail="error creating model")