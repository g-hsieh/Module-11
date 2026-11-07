def compDiscount(quantity, price, discountRate):
    Total = quantity * price
    discountAmount = Total * discountRate
    discountedPrice = Total - discountAmount 
    discountRate = discountRate / 100
    return discountAmount, discountedPrice

# Main Program
quantity = float(input("What is the quantity? "))
price = float(input("What is the price? $"))
discountRate = float(input("Enter the discount rate (%): ")) / 100

discountAmount, discountedPrice = compDiscount(quantity, price, discountRate)

print("\nQuantity\t\t{:,.2f}".format(quantity))
print("Price\t\t\t${:,.2f}".format(price))
print("Discount Amount\t\t${:,.2f}".format(discountAmount))
print("Discounted Price\t${:,.2f}".format(discountedPrice))