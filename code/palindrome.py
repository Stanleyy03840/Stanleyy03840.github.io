class palindrome():
    def __init__(self,string):
        self.string = string
    def __call__(self):
        testStr = self.string.lower()
        for x in [" ","!",]:
          testStr = testStr.replace(x,"")
        if testStr == testStr[::-1]:
            return True
        else:
            return False
def printpal():
    string = input(" What phrase do you want to test? ")
    pal = palindrome(string)
    if pal():
        print("That is a palindrome ")
    else:
        print("That is not a palindrome")
def paltest():
      printpal()
      pal = palindrome("mom")
      print("mom is a palindrome = ", pal())    
      pal2 = palindrome("hotdog")
      print("hotdog is a palindrome = ", pal2())
      pal3 = palindrome("Yo banana boy!")
      print("Yo banana boy! is a palindrome = ", pal3())
if __name__ == "__main__":
    paltest()
