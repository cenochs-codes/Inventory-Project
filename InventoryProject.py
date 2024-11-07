#constants declaration
VALID_CHOICES = ["P", "A", "S", "X"]

InvList = [["Memory", "G.Skill", "DDR4-3200-16GB", 46], ["Power Supply", "Corsair", "CX500", 74], ["Case", "Fractal Design", "Define-R5", 32]]


#We will need to define a function for printing the inventory
def printInventory(list):
    pass

def addItemToInventory(list):
    pass

def sortInventory(list):
    pass

#Create the UI for the program
def printMenu():
    print("***********************************************")
    print("*                                             *")
    print("*           INVENTORY MANAGEMENT              *")
    print("*                                             *")
    print("*           (P)rint Inventory                 *")
    print("*           (A)dd Item to Inventory           *")
    print("*           (S)ort Inventory by Category      *")
    print("*          E(X)it Program                     *")
    print("*                                             *")
    print("***********************************************")

def stringValidation(word):
    pass

def intValidation(num):
    pass

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

