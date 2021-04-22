from pydantic import BaseModel


class Path(BaseModel):
    """
        A class  used to store all necessary paths
    """
    model_dir: str
