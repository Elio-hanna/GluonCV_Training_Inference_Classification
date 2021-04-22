import json
from domain.services.abstract_path_service import AbstractPathService
from domain.models.path import Path


class PathService(AbstractPathService):
    """
     A class used to get paths from path.json and return object of type Paths

    ...

    """

    def __init__(self):
        with open("assets/path.json", 'r') as paths_file:
            json_path = json.load(paths_file)
            self.paths: Path = Path.parse_obj(json_path)

    def get_paths(self) -> Path:
        return self.paths
