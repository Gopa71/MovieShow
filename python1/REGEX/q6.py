# Matching IP Addresses: Create a regex pattern to match valid IPv4 addresses, such as "192.168.1.1" but not "256.0.0.1" or "192.168.1.1.1"
import re
d="^(\d{2})$|(1[00-99]$)"
if re.search(d,"100"):
    print("match")
else:
    print("not match")
