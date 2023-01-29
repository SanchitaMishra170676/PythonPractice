def sumOfNaturalNumbers(num):
    if num == 0:
        return 0
    return num + sumOfNaturalNumbers(num-1)

print(sumOfNaturalNumbers(10))
