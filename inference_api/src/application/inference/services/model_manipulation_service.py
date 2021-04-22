import os

class ModelManipulationService:

    @staticmethod
    def load_model(model, path):
        try:
            model.load_parameters(os.path.join(path,model))
        except Exception as ex:
            raise ex