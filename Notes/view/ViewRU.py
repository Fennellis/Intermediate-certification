from Note import Note
from view.View import View


class ViewRU(View):
    def menu():
        print("Выберите команду:\n" +
              "1. Создать заметку\n" + 
              "2. Изменить заметку\n" + 
              "3. Удалить заметку\n"+
              "4. Найти заметку\n" +
              "5. Показать все\n" +
              "6. Сменить язык\n"
              "0. Выход")
    
    def create(max_id):
        title = input("Введите заголовок: ")
        body = input("Введите текст: ")
        return Note(max_id + 1, title, body)
    
    def find():
        pass

    def change_language():
        print("Доступные языки: ")