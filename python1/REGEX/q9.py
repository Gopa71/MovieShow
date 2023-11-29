# Password Strength Checker: Create a regex pattern to validate passwords. Ensure they have at least eight characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character.
import re
d="^(\d[a-zA-Z]\w+\w+$)"
if re.search(d,"Abin_12345678"):
    print("match")
else:
    print("not match")