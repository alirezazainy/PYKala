import termcolor2

def mainMenu() :
    print("%----------------MainMenu----------------%\n1.Register\n2.Login\n3.Store\n4.Exit")
    _stc = int(input("Please enter your choose :\n"))
    
    if _stc == 1 :
        pass
        mainMenu()
    elif _stc == 2 :
        pass
        mainMenu()
    elif _stc == 3 :
        pass
        mainMenu()
    elif _stc == 4 :
        exit()  
    else :
        print(termcolor2.colored("<----------------!Invalid Input!---------------->","red"))
        mainMenu()


def Register() : 
    
