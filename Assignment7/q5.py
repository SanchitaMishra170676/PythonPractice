n = int(input("Enter the row size: "))
st = 1
for i in range(0,n):
    for j in range(0,n-1-i):
        print(" ",end='')
    for j in range(0,st):
        print("*",end='')
    st += 2
    print()
