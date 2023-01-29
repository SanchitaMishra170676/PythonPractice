message = input("Enter a message\n")
message = message.lower()
if "please subscribe" in message:
    spam = True
elif "click download" in message:
    spam = True
else:
    spam = False

if spam:
    print("This is a spam message")
else:
    print("Not a spam message")