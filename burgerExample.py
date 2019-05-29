def printMenu():
    print("Welcome to Bill's Blue Burgers!")
    print("Menu: ")
    print("Beef Blue Burger       $3.90")
    print("Turkey Blue Burger     $3.45")
    print("Vegie Blue Burger      $2.50")
    print("Drink and fires        $4.23")


def orderQty():
    #take in a qty from user and then store it in a list that is returned 
    blueBurger = float(input("How many Beef Blue Burgers would you like? "))
    turkeyBurger = float(input("How many Turkey Blue Burgers would you like? "))
    vegieBurger = float(input("How many Vegie Blue Burgers whould you like? "))
    friesDrink = float(input("How many fries and drink sides would you like? "))
    qtyList = [blueBurger, turkeyBurger, vegieBurger, friesDrink]
    return qtyList

def calculate(qty):
    #for loop that iterates both list and multiples qty and price
    priceList = [3.90, 3.45, 2.20, 4.23]
    total = 0
    for idx in range(4):
        increasePurchase = qty[idx] * priceList[idx]
        total = total + increasePurchase
    return total

    
def main():
    printMenu()

    #function call calls another function for list
    orderTotal = calculate(orderQty())

    #uses variable order total to print answer from function call
    print("Your total is ", orderTotal)

main()





