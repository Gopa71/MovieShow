# Matching Markdown Headings: Write a regex pattern to match Markdown headings of various levels (e.g., "## Heading 2" or "### Heading 3"). Extract the heading text and its level.
import re
d="([a-zA-Z]\w+|[1-9]$)"
x=re.findall(d,"#Loging 1,##Loging 2,###Loging 3")
print(x)
