# Extracting Numbers from a String: Given a string containing numbers and text, write a Python program to extract all the numbers using regex.
import re
d="\d\w+"
x=re.findall(d,"enter your lomge22 d234 34 rd")
print(x)