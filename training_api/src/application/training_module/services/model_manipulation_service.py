class ModelManipulationService:

    @staticmethod
    def save_model(model, path):
        """
        save the model
        """
        try:
            model.save_parameters(path + '.params')
        except Exception as ex:
            raise ex