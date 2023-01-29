listOfNames = []
for i in range(3):
    name = input(f"Enter the {i} name: ")
    listOfNames.append(name)

# for name in listOfNames:
#     if(name.startswith('s')):
#         print(f"Hello {name}")

i = 0
while i<3:
    print(listOfNames[i],end=" ")
    i+=1