import re
# data="(24/10/2022)|(22/12/2023)"
data="(\d{2}/\d{2}/\d{4})"
x=re.findall(data,"This is my date of birth 24/10/2022 and 22/12/2023 is my memoriable")
print(x)