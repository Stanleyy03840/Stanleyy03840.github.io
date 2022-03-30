def swap():
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

if __name__ == "__main__":
    swap()