import re
data="^[a-z]\w+@[eg]\w+\.[a-z]\w+$"
if re.search(data,"rahul@gmail.com"):
    print("valid")
else:
    print("not valid")