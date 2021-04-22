from mxnet.gluon import nn


class ModelCreationService:

    @staticmethod
    def create_model():
        """
        Create the ModelCreationService to be used in Training or Loading
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
            return ex