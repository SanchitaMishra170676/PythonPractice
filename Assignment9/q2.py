with open('Assignment9\poems.txt', 'r') as f:
    data = f.read().lower()

if "twinkle" in data:
    print("Present")
else:
    print("Not Present")