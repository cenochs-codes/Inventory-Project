# Christian Enochs, Xander Gross
# Group Project 2
# November 12, 2024
# This program adds, sorts, and prints elements in a product inventory.
# Developed using Visual Studio Code and GitHub


# Constants Delcaration
VALID_CHOICES = ["P", "A", "S", "X"]

InvList = [["Memory", "G.Skill", "DDR4-3200-16GB", 46], ["Power Supply", "Corsair", "CX500", 74], ["Case", "Fractal Design", "Define-R5", 32]]


# Prints information about each item in the inventory
def printInventory(list):
    print()
    print("Current Inventory:")
    print("------------------")

    # Prints each list and it's info
    for item in list:
        for i in item:
            print(i, end=' ')
        print()

    print()
    input("Press any key to continue ")


# Adds user input as a new item to inventory
def addItemToInventory(list):
    category = stringValidation(input("Enter Category: "), "Category")
    brand = stringValidation(input("Enter Brand: "), "Brand")
    model_num = stringValidation(input("Enter Model Number: "), "Model")
    quantity = intValidation(input("Enter Quantity On-Hand: "))

    # Converts user info into a list, then updates InvList
    new_item = [category, brand, model_num, quantity]
    InvList.append(new_item)

    input("Item Added. Press any key to continue ")


# Sorts list items alphabetically
def sortInventory(list):
    list.sort()
    print("The inventory list is sorted")
    input("Press any key to continue ")


# Creates the UI for the program
def printMenu():
    print("*" * 47)
    print("*", " " * 43 , "*")
    print("*           INVENTORY MANAGEMENT              *")
    print("*", " " * 43 , "*")
    print("*           (P)rint Inventory                 *")
    print("*           (A)dd Item to Inventory           *")
    print("*           (S)ort Inventory by Category      *")
    print("*          E(X)it Program                     *")
    print("*", " " * 43 , "*")
    print("*" * 47)


# Validates user strings when adding to inventory
def stringValidation(word, type):
    while not len(word) > 0:
        print("Invalid Entry. Please try again.")
        if type == "Category":
            word = input("Enter Category: ")
        elif type == "Brand":
            word = input("Enter Brand: ")
        elif type == "Model":
            word = input("Enter Model Number: ")

    # Updates valid string
    return word
        

# Validates user integers when adding to inventory
def intValidation(num):
    while not (num.isdigit() and int(num) >= 0):
        print("Invalid Entry. Please try again.")
        num = input("Enter Quantity On-Hand: ")

    # Updates valid integer
    return num


# Main function
def main():
    running = True

    # Continues to execute the program unless input is x/X
    while running:
        printMenu()
        user_choice = input("Select a Menu Choice: ")
        user_choice = user_choice.upper()
        while user_choice not in VALID_CHOICES:
            print("Invalid Menu Choice. Please try again")
            input("Press any key to continue ")
            printMenu()
            user_choice = input("Select a Menu Choice: ")
            user_choice = user_choice.upper()
        if user_choice == "P":
            printInventory(InvList)
        elif user_choice == "A":
            addItemToInventory(InvList)
        elif user_choice == "S":
            sortInventory(InvList)
        elif user_choice == "X":
            running = False


# Invokes the main function
main()