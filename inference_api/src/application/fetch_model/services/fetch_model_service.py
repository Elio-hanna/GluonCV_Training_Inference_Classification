import os
import json
import uuid


class FetchModelService:
    def __init__(self):
        """
        Sets the models base directory, and initializes some dictionaries.
        Saves the loaded model's hashes to a json file, so the values are saved even though the API went down.
        """
        self.models_dict = {}
        self.path = '/models_hash'
        self.model_hash_path = os.path.join(self.path,'model_hash.json')
        print(self.model_hash_path)
        file_exists = os.path.exists(self.model_hash_path)
        if file_exists:
            try:
                with open(self.model_hash_path) as json_file:
                    self.models_hash_dict = json.load(json_file)
            except:
                self.models_hash_dict = {}
        else:
            with open(self.model_hash_path, 'w'):
                self.models_hash_dict = {}
        self.labels_hash_dict = {}
        self.base_models_dir = '/models'

    def fetch_all_models(self):
        """
        Loads all the available models.
        :return: Returns a List of all models and their respective hashed values
        """
        models = self.list_models()
        for model in models:
            if model not in self.models_hash_dict:
                self.get_uuid(model)
        for key in list(self.models_hash_dict):
            if key not in models:
                del self.models_hash_dict[key]

        with open(self.model_hash_path, 'w') as fp:
            json.dump(self.models_hash_dict, fp)
        return self.models_hash_dict

    def list_models(self):
        """
        Lists all the available models.
        :return: List of models
        """
        return [files for files in os.listdir(self.base_models_dir)]

    def get_uuid(self, model):
        """
        get all models in folder saved_model
        :param:
        :return: str of all models available
        """
        if model.endswith(".params"):
            self.models_hash_dict[model] = str(uuid.uuid4())
