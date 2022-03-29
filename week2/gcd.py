def igcd(num1, num2):
    if num1 > num2:
        x = num2
    else:
        x = num1
    for i in range(1, x + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    return gcd


class Gcd:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def __call__(self):
        if self.x > self.y:
            x = self.y

        if self.y > self.x:
            x = self.x

        for i in range(1, x + 1):
            if self.x % i == 0 and self.y % i == 0:
                gcd = i
        return gcd


def gcdtest():
    int1 = int(input("Enter a number"))
    int2 = int(input("Enter another number"))
    try:
        print("The gcd of", int1, "and", int2, "is ", end="")
        print(igcd(int1, int2))
    except:
        print("Sorry, something went wrong")


if __name__ == "__main__":
    gcdtest()
