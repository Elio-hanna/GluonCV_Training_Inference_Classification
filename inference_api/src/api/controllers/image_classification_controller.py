from fastapi import APIRouter, HTTPException, File, UploadFile
from application.inference import inference

import io
import cv2
from starlette.responses import StreamingResponse

router = APIRouter()


@router.post('/models/{model_name}/image_classification')
async def image_classification(model_name: str, input_data: UploadFile = File(...)):
    """
    Segment the Image and return the result as image
    :param model_name: Model name
    :param input_data: Image file
    :return: Image file
    """
    try:
        result = inference.Inference()
        result.image_inference(model_name=model_name, input_data=input_data)
        # img = cv2.imread('result.png')
        file_like = open('result.png', mode="rb")
        return StreamingResponse(file_like, media_type="image/jpeg")
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=300, detail="error")
