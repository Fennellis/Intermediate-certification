from Note import Note
from view.View import View


class ViewEN(View):
    def menu():
        print("Select command:\n" +
                "1. Create a note\n" +
                "2. Edit note\n" +
                "3. Delete note\n"+
                "4. Find note\n" +
                "5. Show all\n" +
                "6. Change language\n" +
                "0. Exit")
    
    def create(max_id):
        title = input("Enter title: ")
        body = input("Enter text: ")
        return Note(max_id + 1, title, body)
    
    def edit() -> tuple[int, str]:
        print("Select the parameter to change:\n" +
              "1. Title\n" +
              "2. Text")
        param = input("-> ")
        try:
            param = int(param)
            if (param != 1 and param != 2):
                return
        except ValueError:
            return
        print("Enter a new value:")
        value = input()

        return (param, value)
    
    def find():
        search = input("Enter part of the text: ")
        return search
    
    def change_language():
        print("Available languages: ")

    def empty_list():
        print("List is empty")