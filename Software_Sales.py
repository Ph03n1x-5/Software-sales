def toFixed(value, digits):
    return "%.*f" % (digits, value)

discountAmount = 0.00
softwarePurchaseAmount = 0.00
totalAmount = 0.00

# INPUT OPERATIONS
print("What is the retail price of the software package?")
priceSoftware = float(input())
print("Enter the number of software packages you purchased.")
quantity = int(input())
print("")
print("")
print("===================================================================")
print("The Retail Cost Per Software Package = $ " + toFixed(priceSoftware,2))
print("The Quantity / Number of Packages Purchased = " + str(quantity))
print("===================================================================")

# IF STATEMENT TO DETERMINE DISCOUNT RATE OF SOFTWARE
if quantity < 10:
    discountRate = 0.00
else:
    if quantity >= 10 and quantity <= 19:
        discountRate = 0.10
    else:
        if quantity >= 20 and quantity <= 49:
            discountRate = 0.20
        else:
            if quantity >= 50 and quantity <= 99:
                discountRate = 0.30
            else:
                if quantity >= 100:
                    discountRate = 0.40

# Calculate discount amount
discountAmount = discountRate * quantity * priceSoftware

# Calculate original amount of software purchase
softwarePurchaseAmount = quantity * priceSoftware

# Calculate the total amount of software purchase after the discount
totalAmount = softwarePurchaseAmount - discountAmount

# OUTPUT RESULTS
print("===================================================================")
print("The Discount % rate = " + toFixed(discountRate * 100,2) + "%")
print("The Calculated DiscountAmount= $ " + toFixed(discountAmount,2))
print("Actual Amount of software purchase Before the Discount = $ " + toFixed(softwarePurchaseAmount,2))
print("Total Amount of software purchase After the Discount = $ " + toFixed(totalAmount,2))
print("===================================================================")

# END PROGRAM
