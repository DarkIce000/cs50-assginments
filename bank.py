#get user input

answer = input('Greeting please: ')

#printing money owes
if answer.startswith("hello"):
    print('$0')
elif  answer.startswith("h"):
    print('$20')
else:
    print('$100')