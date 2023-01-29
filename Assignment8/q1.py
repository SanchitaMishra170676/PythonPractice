def maximum(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1)
        else:
            print(num3)
    else:
        if num2>num3:
            print(num2)
        else:
            print(num3)

maximum(5,5,5)
print(maximum(8,7,6)) #prints none as return type is none