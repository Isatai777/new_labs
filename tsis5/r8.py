import re
s = "HelloHowAreYou Good good"
reg = re.compile('[A-Z][^A-Z]*')
result = reg.findall(s)
print(*result)