from Controller import Controller
from view.ViewEN import ViewEN
from view.ViewRU import ViewRU

running = True
ctrl = Controller({"RU": ViewRU, "EN": ViewEN}, "test.txt")
while (running):
    print("\033[H\033[J")
    ctrl.menu()
    choice = input()
    print("\033[H\033[J")

    match(choice):
        case "1":
            ctrl.create()
        case "2":
            ctrl.edit()
        case "3":
            ctrl.delete()
        case "4":
            pass
        case "5":
            ctrl.show()
            input()
        case "6":
            ctrl.change_language()
        case "0":
            running = False
            ctrl.print_to()
            print("\033[H\033[J")