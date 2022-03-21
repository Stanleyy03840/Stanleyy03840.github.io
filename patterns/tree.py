import time
import os

height = int(input("Enter a number for height: "))

stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
print((' ' * height) + '|')