def swap(age1, age2):
    if age1 > age2:
        x = age1
        age1 = age2
        age2 = x
    return "Numbers are " + str(age1) + " " + str(age2)


age1 = input("Input a value for age1: ")
age2 = input("Input a value for age2: ")

print(swap(age1,age2))