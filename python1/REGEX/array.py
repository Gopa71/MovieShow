import re 
# data="[ce]at"
# if re.match(data,"cat eat meat"):
# data="[ve]at"
# if re.search(data,"cat eat meat"):
data="[A-Z][a-z][a-z][0-9]"
if re.search(data,"Cat9 eat meat"):
    print("true")
else:
    print("false")