# Matching Phone Numbers: Create a regex pattern to match phone numbers in different formats, such as (123) 456-7890, 123-456-7890, 123.456.7890, or 1234567890.
import re
d="^(\(\d{3}\)\s\d{3})-(\d{4}$)|(\d{3})-(\d{3})-(\d{4}$)|(\d{3}\.\d{3}\.\d{4}$)|[1\w+]{10}$"
if re.search(d,"12345678901"):
    print("match")
else:
    print("Not match")