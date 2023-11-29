# Matching Time Format: Create a regex pattern to match time in 12-hour format, like "1:30 PM" or "11:45 AM". Extract the hour, minute, and AM/PM information
import re
d="^([1-9]|1[012]):(\d|1[0-9]|2[0-9]|3[0-9]|4[0-5])(AM|PM)$"
x=re.findall(d,"11:45AM")
print(x)