name = "Sanchita"
date = "28 Jan 2023"
letter = f'''Dear  {name}
You are selected!
{date}
''' 
# letter = letter.replace("<name>",name)
# letter = letter.replace("<date>", date)
print(letter)
print(letter.find("  "))
letter = letter.replace("  "," ")
print("After replacing", letter.find("  "))