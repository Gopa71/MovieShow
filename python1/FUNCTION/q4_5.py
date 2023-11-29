# 5. Create a function calculate_discount that takes the original price and a discount percentage as arguments, and returns the discounted price.
def price(a,b):
    return a-(b/100)*a
s=price(100,20)
print(s)