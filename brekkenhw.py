#add preamble here

#declareGlobals here
def declareGlobals():
    global pizza, fries, drinks, tax
    pizza = 5.95
    fries = 3.95
    drinks = 2.75
    tax = 0.085


def main():

    #initialize globals
    declareGlobals()

    #declare local quantity variables
    qtPizza = 0
    qtFries = 0
    qtDrinks = 0

    #loop main tasks
    flag = True
    while flag:
        selection = displayMenu()

        if selection == "p":
            qtPizza = getQuantity("Pizza slices")
        elif selection == "f":
            qtFries = getQuantity("Fries")
        elif selection == "d":
            qtDrinks = getQuantity("Drinks")
        elif selection == "e":
            flag = False
        else:
            printBill(qtPizza, qtFries, qtDrinks)
            qtPizza = 0
            qtFries = 0
            qtDrinks = 0

def displayMenu():
    print("****** My Fast Food Hut ******")
    print("        P)izza slice")
    print("        F)ries")
    print("        D)rinks")
    print("        T)otal")
    print("        E)xit")
    print("")

    selection = input("Enter letter: ")

    if selection in ['p','f','d','e','t']:
        return selection
    else:
        printError(selection)
        displayMenu()


def printBill(qtPizza, qtFries, qtDrinks):
    total_before_tax = (qtPizza * pizza) + (qtFries * fries) + (qtDrinks * drinks) 
    bill_tax = round(total_before_tax * tax, 2)
    total = round(total_before_tax + bill_tax, 2)

    print("")
    print("Item               Qty         Price")
    print("Pizza slices        {p_q}          {p_p}".format(p_q=qtPizza, p_p=pizza))
    print("Fries               {f_q}          {f_p}".format(f_q=qtFries, f_p=fries))
    print("Drinks              {d_q}          {d_p}".format(d_q=qtDrinks, d_p=drinks))
    print("Tax                            {t}".format(t=bill_tax))
    print("                         ----------")
    print("Total                         {tot}".format(tot=total))
    print("                         ==========")


def getQuantity(food_item):
    if food_item == "Pizza slices":
        return int(input("How many Pizza slices?: "))
    elif food_item == "Fries":
        return int(input("How many Fries?: "))
    elif food_item == "Drinks":
        return int(input("How many Drinks?: "))
    else:
        print("Error: Recieved string not matched by getQuantity function")

def printError():
    print("Error: Not valid selection. Valid selections are: p, f, d, t, or e")
    print("")


if __name__ == "__main__":
    main()