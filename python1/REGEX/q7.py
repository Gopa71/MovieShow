# Matching URLs: Write a regex pattern to match URLs, including both HTTP and HTTPS. It should match "https://www.example.com" and "http://subdomain.example.com/page", but not "ftp://example.com" or "www.example".
import re
d="^(https://)(www\.)([a-z]\w+\.)([a-z]\w+$)|(http://)(subdomain\.)([a-z]\w+\.)([a-z]\w+)/([a-z]\w+$)"
if re.search(d,"http://subdomain.example.com/page"):
    print("match")
else:
    print("Not match")