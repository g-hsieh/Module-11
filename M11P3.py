def compute_Commission(Sales):
    """Calculate the commission:
       10% for sales over $100,000
       5% for sales at or under $100,000
    """
    if Sales > 100000:
        Commission = Sales * 0.10
    else:
        Commission = Sales * 0.05
    return Commission

def compute_NextYearTarget(Sales):
    """Calculate next year's target as 5% more than current sales."""
    NextYearTarget = Sales * 1.05
    return NextYearTarget

# Main Program
lastName = input("What's your last name? ")
Sales = float(input("What's your sales for the month? $"))

Commission = compute_Commission(Sales)
NextYearTarget = compute_NextYearTarget(Sales)

print()
print(f"Salesperson with the last name of {lastName}.")
print(f"Sales: ${Sales:,.2f}")
print(f"Commission: ${Commission:,.2f}")
print(f"Next year's target: ${NextYearTarget:,.2f}")