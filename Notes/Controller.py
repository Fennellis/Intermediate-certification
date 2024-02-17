from Note import Note
from interfaces.IController import IController
from view.View import View

class Controller(IController):

    def __init__(self, views: dict[str, View], path) -> None:
        self.views = views
        self.current_view = list(views.values())[0]
        self.__path = path

        f = open(self.__path, "r")
        lst = f.readlines()
        if lst.__len__() / 4 != 1:
            raise Exception      # обработать некорректное количество строк в файле
        
        self.__db = list()
        pos = 1
        for item in lst:
            item = item.replace("\n", "")
            match(pos):
                case 1:
                    id = item
                case 2:
                    time = item
                case 3:
                    title = item
                case 4:
                    self.__db.append(Note(id, title, item, time))
                    pos = 1
            pos += 1
    
    def menu(self):
        self.current_view.menu()
    
    def create(self):
        if self.__db.__len__() != 0:
            max_id = 0
            for item in self.__db:
                if isinstance(item, Note):
                    max_id = max(max_id, item.id)
            self.db.append(self.current_view.create(max_id))
        else:
            self.db.append(self.current_view.create(0))
    
    def edit(self):
        pass

    def delete(self):
        pass

    def find():
        pass

    def show(self):
        if self.__db.__len__() != 0:
            for item in self.__db:
                if isinstance(item, Note):
                    print(item.to_string())
        else:
            print("Список пуст") # Локализовать

    
    def change_language(self):
        self.current_view.change_language()
        pos = 1
        key_list = list(self.views.keys())
        for language in key_list:
            print(f"{pos}. {language}")
            pos += 1
        choise = int(input())                                     # обработать ввод
        self.current_view = self.views.get(key_list[choise-1])

    def print_to(self):
        f = open(self.__path, "w")
        for item in self.__db:
            if isinstance(item, Note):
                f.write(item.to_string() + "\n")

    # def scan(self):
    #     f = open(self.__path, "r")
    #     lst = f.readlines()
    #     if lst / 4 != 0:
    #         raise Exception      # обработать некорректное количество строк в файле
        
    #     temp = list()
    #     pos = 1
    #     for item in lst:
    #         match(pos):
    #             case 1:
    #                 id = item
    #             case 2:
    #                 time = item
    #             case 3:
    #                 title = item
    #             case 4:
    #                 temp.append(Note(id, title, item, time))
    #                 pos = 1
    #         pos += 1
    #     return temp