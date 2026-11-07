#Global Variables
Total = 0
Tax = 0

def compute_Total(quantity, unitPrice):
    '''Calculate the total to enter the quantity and the unit price.'''
    global Total
    Total = quantity * unitPrice
    return Total

def compute_Tax(Total):
    '''Calculate the Tax by multiplying 7% of the total.'''
    global Tax
    Tax = 0.07 * Total
    return Tax

#Main Program
Quantity = int(input("What's the quantity amount? "))
unitPrice = int(input("How much does the unit price cost? "))

compute_Total(Quantity, unitPrice)
compute_Tax(Total)

print(f"The total cost is ${Total:,.2f} while the tax cost is ${Tax:,.2f}.")