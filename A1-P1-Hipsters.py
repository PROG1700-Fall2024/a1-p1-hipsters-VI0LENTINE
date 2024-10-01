#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Customer name (user input)
    print("Welcome to Hipster's Local Vinyl Records! \nDelivery is charged at a rate of $15/km.")
    name = input("Please enter your name: ")

    # Distance user input (kilometers)
    kilometers = input("Please enter distance from Hipster's Local Vinyl Records in kilometers: ")
    kilometers = float(kilometers)
    dCost = kilometers * 15

    # Cost of purchased records, user input
    cost = input("Please insert the cost of your purchase here: ")
    cost = float(cost)
    pCost = cost * 1.14

    # Total cost
    tCost = dCost + pCost

    # Name, delivery cost, records cost (plus tax) and total cost
    print("The name you inserted was: ", name)
    print("Your delivery fees are: ", round(dCost, 2))
    print("Your purchase cost (plus tax) is: ", round(pCost, 2))
    print("Your total is: ", round(tCost, 2))

    # YOUR CODE ENDS HERE

main()