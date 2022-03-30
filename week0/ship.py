import os
import time
def printShip():
    distance = int(input("How far should the ship go? "))
    for x in range(int(distance)):
        print("  "*x,"    |\ ")
        print("  "*x,"    |/ ")
        print("  "*x,"\__ |__/ ")
        print("  "*x," \____/ ")
        print("\u001b[34m {dashes} \u001b[37m".format(dashes = "--"*distance))
        os.system("clear")
        time.sleep(0.006)
if __name__ == "__main__":
    printShip()
