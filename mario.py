height = input("height: ")
while not height.isnumeric() or int(height) <= 0:
    height = input("height: ")

for i in range(1, int(height) + 1):
    for j in range(int(height) - i):
        print(" ", end ="")
    for k in range(int(i)):
        print("#", end ="")
    print("\n")


