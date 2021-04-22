import pydantic
from pydantic import BaseModel


class ParameterInformation(BaseModel):
    """
        A class  used to store the user requested parameter
    """
    name: str = pydantic.Field(default="test", example="test")
    batch: int = pydantic.Field(default=250, example=250)
    learning_rate: float = pydantic.Field(default=0.001, example=0.001)
    epchs: int = pydantic.Field(default=10, example=10)