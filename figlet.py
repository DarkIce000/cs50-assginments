#libraries
import sys
import random
from pyfiglet import Figlet


#getting list of available fonts
figlet = Figlet()
my_list = figlet.getFonts()

#expect two argument 1. --f or font
if (len(sys.argv) == 2) or (len(sys.argv) == 3):
    #checking for correct letter or word
    if sys.argv[1] == "--f" or sys.argv[1] == "--font":
        #checking for font present or not
        if (sys.argv[2]) in my_list:
            answer = input("type: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(answer))
        elif not sys.argv[2] in my_list:
            print("invalid usage")
            sys.exit(3)

    elif sys.argv[1] == "0":
        #chose random font and set then print
        answer = input ("type: ")
        random_selected = random.choice(my_list)
        figlet.setFont(font= random_selected)
        print(figlet.renderText(answer))
    else:
        print("invalid usage")
else:
    print("invalid usage")
    sys.exit(1)




