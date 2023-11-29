# Matching Hashtags: Write a regex pattern to match hashtags in a text, such as "#Python" or "#RegexPractice". Extract all hashtags from a given string.
import re
d="#[a-zA-Z]\w+"
x=re.findall(d,"asbinnns #Abin #gop")
print(x)