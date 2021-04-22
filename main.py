from training_api.src.application.training_module import Train_model
from inference_api.src.prediction_module import load_model
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException

from inference_api.src.services import fetch_model_service, logging_service


class param(BaseModel):
    name: str
    learning_rate: Optional[float] = None
    batch: Optional[float] = None
    epchs: Optional[int] = None


app = FastAPI()
logging = logging_service.LoggingService()


@app.post("/train_model/")
async def create_model(item: Optional[param] = None):
    """
    the user submit a json object that contain all the details needed to create and train a model
    :param item:
    :return:
    """
    if item is None:
        return {"name cannot be empty"}
    else:
        Model = Train_model.TrainModel()
        if item.name is None:
            return {"name cannot be empty"}
        name = item.name
        learning_rate = item.learning_rate
        batch = item.batch
        epchs = item.epchs
        if learning_rate == 0 or learning_rate is None:
            learning_rate = 0.001
        if batch == 0 or batch is None:
            batch = 250
        if epchs == 0 or epchs is None:
            epchs = 10
        parr = "learning rate: " + str(learning_rate) + " batch: " + str(batch) + " epochs: " + str(epchs) + " "

        try:
            Model.create_and_train(model_name=name, batch_size=batch, learning_rate=learning_rate, epochs=epchs)
            logging.log(name=create_model.__name__, result="Model saved " + name, parm=parr)
            return {"Model Trained and saved in": name}
        except Exception as ex:
            logging.log_error(create_model.__name__)
            raise HTTPException(status_code=404, detail="error creating model")


@app.get("/train/{model_name}")
async def create_train_save(model_name):
    """
    Create a Model and train it then save it to a file given in param
    :param model_name: model name given by the user
    :return:  message
    """
    learning_rate = 0.001
    batch = 250
    epchs = 1
    parr = "learning rate: " + str(learning_rate) + " batch: " + str(batch) + " epochs: " + str(epchs) + " "
    print(parr)
    Model = Train_model.TrainModel()
    try:
        Model.create_and_train(model_name=model_name, batch_size=batch, learning_rate=learning_rate, epochs=epchs)
        logging.log(name=create_model.__name__, result="Model saved " + model_name + ".params", parm=parr)
        return {"Model Trained and saved in": model_name}
    except Exception as ex:
        logging.log_error(name=create_train_save.__name__)
        raise HTTPException(status_code=404, detail="error creating model")


@app.get("/models")
async def show_models():
    """
    load all Models available in /assets/model
    :return: names
    """
    try:
        Model = fetch_model_service.FetchModelService()
        result = Model.get_all_models()
        logging.log(name=show_models.__name__, result=result)
        return {"The loaded model are": result}
    except Exception as ex:
        raise HTTPException(status_code=300, detail="cannot show models")


@app.post("/predict/")
async def predict(model: str, image_name: str):
    """
    load the model specified and predict what is the image given by the user
    :param model: model name
    :param image_name: image given by the user
    :return: the prediction value
    """
    Model = load_model.load_model()
    try:
        prediction = Model.predict(model_name=model, file=image_name)
        parr = "model used: " + model + " "
        logging.log(name=predict.__name__, result=prediction, parm=parr)
        return {"Prediction": prediction}
    except Exception:
        logging.log_error(name=predict.__name__)
        raise HTTPException(status_code=300, detail="cannot predict")