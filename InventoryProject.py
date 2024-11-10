# NAMES
# PROJECT TITLE
# DATE
# PROJECT FUNCTION
# DEVELOPED USING...


#constants declaration
VALID_CHOICES = ["P", "A", "S", "X"]

InvList = [["Memory", "G.Skill", "DDR4-3200-16GB", 46], ["Power Supply", "Corsair", "CX500", 74], ["Case", "Fractal Design", "Define-R5", 32]]


#We will need to define a function for printing the inventory
def printInventory(list):
    print()
    print("Current Inventory:")
    print("------------------")
    for item in list:
        for i in item:
            print(i, end=' ')
        print()
    print()
    input("Press any key to continue ")


def addItemToInventory(list):
    category = stringValidation(input("Enter Category: "), "Category")
    brand = stringValidation(input("Enter Brand: "), "Brand")
    model_num = stringValidation(input("Enter Model Number: "), "Model")
    quantity = intValidation(input("Enter Quantity On-Hand: "))

    new_item = [category, brand, model_num, quantity]
    InvList.append(new_item)

    input("Item Added. Press any key to continue ")


def sortInventory(list):
    list.sort()
    print("The inventory list is sorted")
    input("Press any key to continue ")


#Create the UI for the program
def printMenu():
    print("*" * 47)
    print("*                                             *")
    print("*           INVENTORY MANAGEMENT              *")
    print("*                                             *")
    print("*           (P)rint Inventory                 *")
    print("*           (A)dd Item to Inventory           *")
    print("*           (S)ort Inventory by Category      *")
    print("*          E(X)it Program                     *")
    print("*                                             *")
    print("*" * 47)


def stringValidation(word, type):
    while not len(word) > 0:
        print("Invalid Entry. Please try again.")
        if type == "Category":
            word = input("Enter Category: ")
        elif type == "Brand":
            word = input("Enter Brand: ")
        elif type == "Model":
            word = input("Enter Model Number: ")

    return word
        

def intValidation(num):
    while not (num.isdigit() and int(num) >= 0):
        print("Invalid Entry. Please try again.")
        num = input("Enter Quantity On-Hand: ")

    return num


def main():
    running = True
    while running:
        printMenu()
        user_choice = input("Select a Menu Choice: ")
        user_choice = user_choice.upper()
        while user_choice not in VALID_CHOICES:
            print("Invalid Menu Choice. Please try again")
            printMenu()
            user_choice = input("Select a Menu Choice: ")
            user_choice = user_choice.upper()
        if user_choice.upper() == "P":
            printInventory(InvList)
        elif user_choice == "A":
            addItemToInventory(InvList)
        elif user_choice == "S":
            sortInventory(InvList)
        elif user_choice == "X":
            running = False


main()



