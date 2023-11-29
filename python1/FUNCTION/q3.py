# Create a function , and calculated using the formula: 
# Final Price(FP) = (Product Price of of X )/(Product Price of Y)^2. 
# Write python code which can accept the price X and price of Y of a 
# Product and calculate the FP. Note: Make sure to use a function 
# which accepts the X and Y values and returns the FP value.
x=int(input("Enter the 1st product price : "))
y=int(input("Enter the 2nd product price : "))
def price(x,y):
    fp=(x/y)**2
    return fp
print("The final price is :",price(x,y))