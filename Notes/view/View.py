from abc import ABC, abstractmethod

from Note import Note


class View(ABC):
    
    @abstractmethod
    def menu() -> Note:
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def find():
        pass

    @abstractmethod
    def change_language():
        pass
