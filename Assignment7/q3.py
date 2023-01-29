import math
num = int(input("Enter the number: "))
prime = True
for i in range(2,int(math.sqrt(num))):
    if num%i == 0:
        prime = False

if prime:
    print("PRIME")
else:
    print("NOT PRIME")