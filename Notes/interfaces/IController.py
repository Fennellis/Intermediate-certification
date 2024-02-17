from abc import ABC, abstractmethod


class IController(ABC):

    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def edit():
        pass

    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def show():
        pass
    
    @abstractmethod
    def find():
        pass

    @abstractmethod
    def change_language():
        pass