#get user input

answer = input('Greeting please: ')
usrinput = answer.lower()
#printing money owes
if usrinput.startswith("hello") or usrinput.startswith(" hello ") or usrinput.startswith(" hello"):
    print('$0')
elif  usrinput.startswith("h"):
    print('$20')
else:
    print('$100')