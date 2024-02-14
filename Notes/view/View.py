from abc import ABC, abstractmethod


class View(ABC):
    
    @abstractmethod
    def Menu():
        pass

    @abstractmethod
    def Create():
        pass

    @abstractmethod
    def Find():
        pass

    @abstractmethod
    def ChangeLanguage():
        pass
