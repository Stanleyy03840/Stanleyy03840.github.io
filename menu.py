from week0.christmastree import printTree
from week0.ship import printShip
from week0.swap import swap
from week0.matrix import print_matr
from week1.fibonacci import printFibo
from week1.lists import InfoDb
from week2.factorial import printFact
from week1.loops import for_loop,while_loop,recursive_loop
from week2.gcd import gcdtest
from week2.palindrome import paltest
from week3.factor import normal_factor

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    while choice not in menu:
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()

        else:
            presentMenu(menu[choice]["exec"])
mathMenu = {
    1: {
        "display":"Fibonacci",
        "exec": printFibo,
        "type":"func"
    },
    2: {
        "display": "Factorial",
        "exec":printFact,
        "type":"func"
    },
    3: {
        "display": "GCD",
        "exec":gcdtest,
        "type":"func"
    },
    4: {
        "display": "Factor",
        "exec":normal_factor,
        "type":"func"
    },
    5: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

hack2Menu = {
    1: {
        "display":"For loop",
        "exec": for_loop,
        "type":"func"
    },
    2: {
        "display":"While loop",
        "exec": while_loop,
        "type":"func"
    },
    3: {
        "display":"Recursive",
        "exec": recursive_loop,
        "type":"func"
    },
    4: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}
drawingMenu = {
    1: {"display":"Christmas Tree",
    "exec":printTree,
    "type":"func"},
    2: {"display":"Ship",
    "exec":printShip,
    "type":"func"},
    3: {"display":"Matrix",
    "exec":print_matr,
    "type":"func"},
    4: {"display":"Swap",
    "exec":swap,
    "type":"func"},
    5: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

listMenu = {
    1: {"display":"Lists and Loops",
        "exec": hack2Menu,
        "type":"submenu"
       },
    2: {
        "display": "Palindrome",
        "exec":paltest,
        "type":"func"
    },
    3: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    1: {
        "display":"Math Menu",
        "exec": mathMenu,
        "type":"submenu"
    },
    2: {
        "display":"Drawing Menu",
        "exec": drawingMenu,
        "type":"submenu"
    },
    3: {
        "display":"List Menu",
        "exec": listMenu,
        "type":"submenu"
    },
    4: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

if __name__ == "__main__":
  presentMenu(mainMenu)
