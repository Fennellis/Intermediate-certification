from Controller import Controller
from view.ViewEN import ViewEN
from view.ViewRU import ViewRU
running = True
ctrl = Controller({"RU": ViewRU, "EN": ViewEN})
while (running):
    print("\033[H\033[J")
    ctrl.Menu()
    choice = input()
    print("\033[H\033[J")

    match(choice):
        case "1":
            ctrl.Create()
        case "2":
            ctrl.Save()
        case "3":
            ctrl.Show()
        case "4":
            ctrl.Edit()
        case "5":
            ctrl.Delete()
        case "6":
            ctrl.ChangeLanguage()
        case "0":
            running = False
            print("\033[H\033[J")