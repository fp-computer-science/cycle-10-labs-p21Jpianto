# Author: JAP (AMDG) 12/3/20

def sum_to(value):
    total = 0
    for x in range(int(value) + 1):
        total += x
    return total


numbers = input("Give me some numbers")
print(sum_to(numbers))
