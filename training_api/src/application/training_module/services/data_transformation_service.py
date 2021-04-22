from mxnet.gluon.data.vision import transforms

class DataTransformationService:
    def data_transformation(self):
        """
        Transform data so the model can train on it
        """
        try:
            transformer = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(0.13, 0.31)])
            return transformer
        except Exception as ex:
            return ex