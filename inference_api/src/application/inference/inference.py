import os
import numpy as np
import cv2
import mxnet as mx
from mxnet import nd
from mxnet import gluon
from mxnet.gluon import nn
from mxnet.gluon.data.vision import datasets, transforms
from mxnet import image
from fastapi import HTTPException
from PIL import Image,ImageFont, ImageDraw
from application.inference.services import model_service,label_service,model_manipulation_service

class Inference:
    def __init__(self):
        self.path = '/models'

    def loadmodel(self,model_name:str):
        """
        load the chosen model
        :param model_name: name of the model
        :return: the model
        """
        try:
            model = model_service.ModelService()
            load_model = model_manipulation_service.ModelManipulationService()
            net = model.create_model()
            net.load_parameters(os.path.join(self.path,model_name))
            return net
        except Exception as ex:
            raise ex
    
    def loadimage(self,file):
        """
        load the image and transform so we can predict
        :param file: image name
        :return: the final image
        """
        try:
            transform_fn = transforms.Compose([
            transforms.Resize(32),
            transforms.CenterCrop(32),
            transforms.ToTensor(),
            transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])
            ])
            imput = Image.open(file.file, "r").convert('RGB')
            input_im = np.array(imput)  
            img = cv2.cvtColor(input_im, cv2.COLOR_RGB2BGR)
            cv2.imwrite(file.filename, img)
            img = image.imread(file.filename)
            img = transform_fn(img)
            return img
        except Exception as ex:
            raise ex

    def get_prediction(self,pred):
        """
        get the final result of a prediction
        :param pred: int given 
        :return: the final prediction in str
        """
        try:
            lbl = label_service.LabelService()
            
            class_names = lbl.label_text()
            
            ind = nd.argmax(pred, axis=1).astype('int')
            return class_names[ind.asscalar()]
        except Exception as ex:
            raise ex

    def final_result(self,file,prediction):       
        image = cv2.imread(file.filename)
        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)
        draw = ImageDraw.Draw(pil_im)
        draw.text((0, 0), prediction)
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imwrite("result.png", cv2_im_processed)

    def image_inference(self,model_name,input_data):
        """
        the user will give the model name and the image
        :param model_name:model name to be used
        :param file: image to pass to the model
        :return: prediction in str
        """
        try:
            net = self.loadmodel(model_name=model_name)
            pred = net(self.loadimage(file=input_data).expand_dims(axis=0))
            class_name = self.get_prediction(pred)
            self.final_result(input_data,class_name)
            os.remove(input_data.filename)
        except Exception as ex:
            raise ex