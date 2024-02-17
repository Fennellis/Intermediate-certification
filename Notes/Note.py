import datetime

class Note:
    def __init__(self, id, title, body, time = datetime.datetime.now()):
        self.__id = id
        self.__time = time
        self.__title = title
        self.__body = body

    @property
    def id(self):
        return self.__id
    
    @property
    def time(self):
        return self.__time
    @property
    def time(self, time):
        self.__time = time
    @property
    def title(self):
        return self.__title
    @property
    def title(self, title):
        self.__title = title
    @property
    def body(self):
        return self.__body
    @property
    def body(self, body):
        self.__body = body
    
    def to_string(self):
        return f"{self.__id}\n{self.__time}\n{self.__title}\n{self.__body}"