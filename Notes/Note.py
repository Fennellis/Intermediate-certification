import datetime

class Note:
    def __init__(self, id: int, title, body, time = datetime.datetime.now()):
        self.__id = id
        self.__time = time
        self.__title = title
        self.__body = body

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time):
        self.__time = time
    @property
    def title(self) -> str:
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title
    @property
    def body(self) -> str:
        return self.__body
    @body.setter
    def body(self, body):
        self.__body = body
    
    def to_string(self):
        return f"{self.__id}\n{self.__time}\n{self.__title}\n{self.__body}"