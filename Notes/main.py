from Controller import Controller


running = True
ctrl = Controller()

while (running):
    ctrl.Menu()
    choice = input()

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
        case "0":
            running = False