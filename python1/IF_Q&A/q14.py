# 14:Write a program that asks the user to enter their annual income and calculates the income tax they owe using elif statements based on the following income tax brackets:

# Income up to $10,000: No tax
# Income from $10,001 to $50,000: 10% tax
# Income from $50,001 to $100,000: 20% tax
# Income above $100,000: 30% tax
# Display the calculated tax amount.
a=int(input("Enter the annual income : "))
if a>100000:
    print("30% tax")
elif a>=100000:
    print("20% tax")
el