from interfaces.IController import IController
from view.View import View


class Controller(IController):

    def __init__(self, views: dict[str, View]) -> None:
        self.views = views
        self.current_view = list(views.values())[0]
    
    def Menu(self):
        self.current_view.Menu()
    
    def Create(self):
        self.current_view.Create()
    
    def Save(self):
        print("Save")

    def Show(self):
        print("Show")

    def Edit(self):
        print("Edit")

    def Delete(self):
        print("Delete")
    
    def ChangeLanguage(self):
        self.current_view.ChangeLanguage()
        pos = 1
        key_list = list(self.views.keys())
        for language in key_list:
            print(f"{pos}. {language}")
            pos += 1
        choise = int(input())
        self.current_view = self.views.get(key_list[choise-1])