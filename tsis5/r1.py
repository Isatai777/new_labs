import re
s='abb dfab'
reg = re.compile('ab*')
result = reg.findall(s)
print(result)
