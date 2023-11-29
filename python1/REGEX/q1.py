import re
# data="[01-31]{2}-[01-12]{2}-\d{4}"
data="(^[012]\d|3[01])-([0][1-9]|1[012])-(\d{4}$)"
if re.search(data,"31-01-2021"):
    print("true")
else:
    print("false")