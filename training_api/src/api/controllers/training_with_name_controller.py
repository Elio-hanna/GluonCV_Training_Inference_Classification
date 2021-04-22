from application.training_module import train_model
from fastapi import APIRouter,HTTPException

from application.logging.services import logging_service
from DTO.parameter_information import ParameterInformation

router = APIRouter()
logging = logging_service.LoggingService()

@router.post("/train/{model_name}")
async def create_train_save(model_name):
    """
    Create a ModelCreationService and train it then save it to a file given in param
    :param model_name: model name given by the user
    :return:  message
    """
    #learning_rate = 0.001
    #batch = 250
    #epchs = 1
    
    item = ParameterInformation()
    
    item.name = model_name
    
    parr = "learning rate: " + str(item.learning_rate) + " batch: " + str(item.batch) + " epochs: " + str(item.epchs) + " "
    
    Model = train_model.TrainModel()
    try:
        print("here")
        Model.create_and_train(model_name=model_name, batch_size=item.batch, learning_rate=item.learning_rate, epochs=item.epchs)
        # Model.create_and_train(item)
        logging.log(name=create_train_save.__name__, result="ModelCreationService saved " + model_name + ".params", parm=parr)
        return {"ModelCreationService Trained and saved in": model_name}
    except Exception as ex:
        logging.log_error(name=create_train_save.__name__)
        raise HTTPException(status_code=404, detail="error creating model")