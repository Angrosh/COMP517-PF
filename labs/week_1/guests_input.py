import re

print()
print("Please choose one of them")
print("==========================")
print()
print("main, dessert, both, none")
print()


numOfGuests = 3

mainCounter = 0
dessertCounter = 0
guestChoice = {}



for guest_num in range(numOfGuests):
    getInput = input("Guest " + str(guest_num) + ", Enter your input: " )

    if getInput == "main":
        mainCounter += 1
        guestChoice["Guest "+str(guest_num)] = "1 main"

    elif getInput == "dessert":
        dessertCounter += 1
        guestChoice["Guest "+str(guest_num)] = "1 desert"

    elif getInput == "both":
        mainCounter += 1
        dessertCounter += 1
        guestChoice["Guest "+str(guest_num)] = "1 desert, 1 main"

# output section
print()
print("Total number of main courses and desserts")
print("------------------")
print("Number of mains: ", mainCounter)
print("Number of desserts: ", dessertCounter)
print()

print("Guest Preferencses")
print("------------------")
print(guestChoice)
for key, value in guestChoice.items():
    print(key + " : " + value)

print

