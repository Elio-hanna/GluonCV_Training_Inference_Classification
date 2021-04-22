from abc import abstractmethod, ABC, ABCMeta

from domain.models.path import Path


class AbstractPathService(ABC):

    @abstractmethod
    def get_paths(self) -> Path: raise NotImplementedError
