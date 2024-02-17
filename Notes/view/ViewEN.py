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
    
    def find():
        pass
    
    def change_language():
        print("Available languages: ")