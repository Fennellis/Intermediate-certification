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
        if lst.__len__() % 4 != 0:
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
                    pos = 0
            pos += 1
    
    def menu(self):
        self.current_view.menu()
    
    def create(self):
        if self.__db.__len__() != 0:
            max_id = 0
            for item in self.__db:
                if isinstance(item, Note):
                    max_id = max(int(max_id), int(item.id))
            self.__db.append(self.current_view.create(max_id))
        else:
            self.__db.append(self.current_view.create(0))
    
    def edit(self):
        seacrh_list = self.find()
        if (seacrh_list.__len__ == 0):
            self.current_view.empty_list()
            return
        chosen = input("-> ")
        try:
            chosen = int(chosen)
        except ValueError:
            return
        temp = self.current_view.edit()
        for item in self.__db:
            if isinstance(item, Note):
                if (int(item.id) == chosen):
                    match(temp[0]):
                        case 1:
                            item.title = temp[1]
                        case 2:
                            item.body = temp[1]

    def delete(self):
        seacrh_list = self.find()
        if (seacrh_list.__len__ == 0):
            self.current_view.empty_list()
            return
        chosen = input("-> ")
        try:
            chosen = int(chosen)
        except ValueError:
            return
        for item in self.__db:
            if isinstance(item, Note):
                if (int(item.id) == chosen):
                    self.__db.remove(item)

    def find(self) -> list:
        search = self.current_view.find()
        lst_return = list()
        for note in self.__db:
            if isinstance(note, Note):
                if search.lower() in note.title.lower() or search in note.body.lower():
                    print(note.to_string())
                    lst_return.append(note)
        return lst_return

    def show(self):
        if self.__db.__len__() != 0:
            for item in self.__db:
                if isinstance(item, Note):
                    print(item.to_string())
        else:
            self.current_view.empty_list()

    
    def change_language(self):
        self.current_view.change_language()
        pos = 1
        key_list = list(self.views.keys())
        for language in key_list:
            print(f"{pos}. {language}")
            pos += 1
        try:
            choise = int(input())
        except ValueError:
            return
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