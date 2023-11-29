# 13:Create a login program that asks the user to enter their username and password. Use elif statements to check if the entered credentials are correct. If the username and password match predefined values, print "Login successful." Otherwise, print "Login failed."
user_name="Abingop"
password="password"
a=str(input("Enter the user name : "))
b=str(input("Enter the password : "))
if a==user_name and b==password:
    print("Login successful.")
else:
    print("Login failed.")

