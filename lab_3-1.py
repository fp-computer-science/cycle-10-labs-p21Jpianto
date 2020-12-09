# Author:JAP 12/7/2020  (amdg)


def sum_to(n):
    total = 0
    iteration = 1
    while iteration < n+1:
        total += iteration
        iteration += 1
    return total

num = input("Please give a number")

results = sum_to(into(num))
print(results)
