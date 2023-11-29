# 12:Create a program that asks the user to enter the total purchase amount. Depending on the purchase amount, apply a discount using elif statements:

# If the purchase amount is greater than or equal to $100, apply a 10% discount.
# If the purchase amount is greater than or equal to $50, apply a 5% discount.
# If the purchase amount is less than $50, no discount is applied.
# Calculate the final amount after the discount and display it.

a=int(input("Enter the total amount of you purchase : "))
if a>=100:
     print("10%""discount")
elif a>=50:
     print("5%""discount")
elif a<50:
     print("No discount apply")