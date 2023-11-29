'''1. Traffic light'''
# Write a python program that will check for the following conditions:

# If the light is green – Car is allowed to go
# If the light is yellow – Car has to wait
# If the light is red – Car has to stop
# Other signal – unrecognized signal. Example black, blue, etc…
 
a=str(input("Enter The Light Color: "))
if a=="green":
    print("Car is allowed to go")
elif a=="yellow":
    print("Car has to wait")
elif a=="red":
    print("car has to stop")
else:
    print("Unrecognized Signal")
