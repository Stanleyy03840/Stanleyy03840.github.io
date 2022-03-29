from week1.lists import InfoDb

def for_loop():
    for x in InfoDb:
        for key,value in x.items():
            print(f"{key}: {value}")
        print()
        print("-"*10)
        print()

def while_loop():
    x = 0
    while x < len(InfoDb):
        for key,value in InfoDb[x].items():
            print(f"{key}:{value}")
        print()
        print('-'*10)
        print()
        x += 1

def recursive_loop():
    n=0
    if n>= len(InfoDb):
        return 
    else:
        for key,value in InfoDb[n].items():
            print(f"{key}:{value}")
        print()
        print("-"*10)
        print()
        recursive_loop(n+1)

if __name__ == "__main__":
    for_loop()
