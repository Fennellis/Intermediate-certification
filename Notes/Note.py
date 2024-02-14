class Note:
    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body

    @property
    def id(self):
        return self.__id
    @property
    def title(self):
        return self.title
    @property.setter
    def title(self, title):
        self.title = title
    @property
    def body(self):
        return self.body
    @property.setter
    def body(self, body):
        self.body = body
    
    def ToString(self):
        return f"{self.__title}\n{self.__body}"