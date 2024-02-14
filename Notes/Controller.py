from interfaces.IController import IController


class Controller(IController):
    def Menu(self):
        print("Menu")
    
    def Create(self):
        print("Create")
    
    def Save(self):
        print("Save")

    def Show(self):
        print("Show")

    def Edit(self):
        print("Edit")

    def Delete(self):
        print("Delete")