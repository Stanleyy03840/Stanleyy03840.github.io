InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Leo",
    "LastName": "Sun",
    "Favorite Colors":["Red","Orange","Yellow"]
})

InfoDb.append({
    "FirstName": "Stanley",
    "LastName": "Yan",
    "Favorite Colors":["Blue", "Green", "Purple"]
})

InfoDb.append({
    "FirstName": "Ur",
    "LastName": "Mom",
    "Favorite Colors":["Black", "Grey", "White"]
})

def for_loop(): #iterates on length of the list
    for i in range(len(InfoDb)):
        print(InfoDb[i])

def while_loop(): #initial index n and increments by 1
    i = 0
    while i < len(InfoDb):
        print(InfoDb[i])
        i = i+1

def recursive_loop(i = 0): #loop increments on n + 1 until each condition is met
    if i < len(InfoDb):
        print(InfoDb[i])
        recursive_loop(i + 1)

def tester():
    num = int(input("Pick a number for a loop? 1: while, 2: for, 3: recursive"))
    print(num)
    print(type(num))
    if num == 1:
        while_loop()
    elif num == 2:
        for_loop()
    elif num == 3:
        recursive_loop()

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    tester()