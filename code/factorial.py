class Factorial:
	def __call__(self, n):
		if n == 0:
			return 1
		elif n == 1:
			return 1
		else:
			return n * self(n-1)

def tester():
    number = int(input("Enter a number to factorial: "))
    try:
        yeah = Factorial() 
        print("Answer:", yeah(number))   
    except:
        print("Please enter a positive integer.")   

if __name__ == "__main__":
    tester=()
