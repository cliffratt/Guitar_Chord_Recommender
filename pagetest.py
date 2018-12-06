def cls():
    print("\n" * 100)

def welcome_screen():
    cls()
    print('=========================\n')
    print('=====           =========\n')
    print('=====  Welcome  =========\n')
    print('=====           =========\n')
    print('=========================\n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    name = input("What is your name? ")
    print("Your name is: ", name)
    return name

def selection_screen(name):
    cls()
    print('=========================\n')
    print('=====             =======\n')
    print('=====  Selection  =======\n')
    print('=====             =======\n')
    print('=========================\n')
    print('1. Find Guitar Tabs      \n')
    print('2. Exit                  \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    selection = input(f"Hello {name}. What is your selection? ")
    return selection

def survey_screen(name):
    cls()
    print('=========================\n')
    print('=====             =======\n')
    print('=====  Survey     =======\n')
    print('=====             =======\n')
    print('=========================\n')
    print('                         \n')
    print('   Feature Coming Soon!  \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    print('                         \n')
    #selection = input(f"Hello {name}. What is your selection? ")
    #return selection


def mymain():
    name = welcome_screen()
    selection = selection_screen(name)
    if selection == '1':
         survey_screen(name)

mymain()
