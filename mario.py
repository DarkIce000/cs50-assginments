# getting input
height = input("height: ")
# rejecting non integer and <=0 and >= 9
while not height.isnumeric() or int(height) <= 0 or int(height) >= 9:
    height = input("height: ")

# printing # and white space with same logic as done in c
for i in range(1, int(height) + 1):
    for j in range(int(height) - i):
        print(" ", end="")
    for k in range(int(i)):
        print("#", end="")
    print("")

