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
    def edit() -> tuple[int, str]:
        pass
    @abstractmethod
    def find() -> str:
        pass

    @abstractmethod
    def change_language():
        pass
    
    @abstractmethod
    def empty_list():
        pass
