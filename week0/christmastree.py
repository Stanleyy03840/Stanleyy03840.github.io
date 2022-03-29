def printTree():
    import random
    row = int((input("How large should the tree be? ")))
    for x in range(row):
        x+=1
        spaces = row-x
        # output = " "*spaces
        # for y in range(2*x):
        #     output+=random.choice(["\033[0;32m*\033[00m","\033[0;32m*\033[00m","\033[0;32m*\033[00m","\033[0;31m*\033[00m"])
        # print(output)
        print(" "*spaces,"\033[0;32m*\033[00m "*x)
    print(" "*(row-3),"* "*3)
    print(" "*(row-3),"* "*3)
if __name__ == "__main__":
    printTree()
