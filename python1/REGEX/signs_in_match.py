'''import re
data="^[A-Z]"  #^ is use for get first data
if re.match(data,"Cat eat meat"):
    print("true")
else:
    print("false")'''


# import re
# data="meat$"
# if re.search(data,"cat eat meat"):
#     print("true")
# else:
#     print("false")

# import re
# data="meats+"
# if re.search(data,"cat eat meatss"):
#     print("true")
# else:
#     print("false")


import re
data="meat*"
if re.search(data,"cat eat meatsss"):
    print("true")
else:
    print("false")