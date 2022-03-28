def avg(a, b):
    sum = a + b
    avg = sum/2
    return "The average of" + int(a) + "and" + int(b) + "is:"




class Average:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self):
		sum = self.a + self.b
    avg = sum/2
    return avg

def tester():
	num = input("Imperative [i] or OOP [o]")
	try:
		if num == 'i':
      a = int(input("Input an integer "))
      b = int(input("Input another integer: "))
			print("Average:")
			print(avg(a,b)
		elif num == 'o':
			f = Average(int(input("Input an integer")),int(input("Input an integer")))
			print("Average")
			print(f())
	except:
		print("Sorry, something went wrong")


if __name__ == "__main__":
    tester()
