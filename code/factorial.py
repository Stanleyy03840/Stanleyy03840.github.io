class factorial(object):
    def __init__(self,n):
        self.n = n
    def factorial(self, n=None):
        n = self.n if n is None else n
        result = 1
        if self.n == 1:
            result = 1
            return result
        else:
          for x in range(1,n+1):
            result*=x
          return result

def printFact():
    fac1 = factorial(int(input("What number factorial?")))
    fac2 = factorial(1)
    fac3 = factorial(8)
    fac4 = factorial(3)
    print(fac1.factorial())
    print("factorial of 1 is:", fac2.factorial())
    print("factorial of 8 is:", fac3.factorial())
    print("factorial of 3 is:", fac4.factorial())
    

if __name__ == "__main__":
    printFact()
