from mxnet.gluon import nn
from mxnet.gluon.data.vision import transforms
from fastapi import HTTPException


class ModelService:

    @staticmethod
    def create_model():
        """
        Create the Model to be used in Training or Loading
        :return:
            -net: is the model to be returned and used in other functions
            -transformer: transforms the images
        """
        try:
            net = nn.Sequential()
            net.add(nn.Conv2D(channels=6, kernel_size=5, activation='relu'),
                    nn.MaxPool2D(pool_size=2, strides=2),
                    nn.Conv2D(channels=16, kernel_size=3, activation='relu'),
                    nn.MaxPool2D(pool_size=2, strides=2),
                    nn.Flatten(),
                    nn.Dense(120, activation="relu"),
                    nn.Dense(84, activation="relu"),
                    nn.Dense(10))
            return net
        except Exception as ex:
            raise ex

    @staticmethod
    def transformer():
        try:
            transformer = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(0.13, 0.31)])
            return transformer
        except Exception as ex:
            raise ex