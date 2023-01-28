dict = {
    "namaste": "hello",
    "kitab" : "book",
}
word = input("Enter the hindi word ")
# print("Meaning: ", dict[word])
print(dict.get(word)) #No error if key is not present