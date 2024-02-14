from abc import ABC, abstractmethod


class IController(ABC):

    @abstractmethod
    def Menu(self):
        pass

    @abstractmethod
    def Create():
        pass

    @abstractmethod
    def Save():
        pass

    @abstractmethod
    def Show():
        pass

    @abstractmethod
    def Edit():
        pass

    @abstractmethod
    def Delete():
        pass