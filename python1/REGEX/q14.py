# Matching Social Security Numbers: Write a regex pattern to match and validate U.S. Social Security Numbers in the format XXX-XX-XXXX
import re
d="^([0-9]{3})-([0-9]{2})-([0-9]){4}$"
if re.search(d,"123-12-2345"):
    print("Match")
else:
    print("Not match")