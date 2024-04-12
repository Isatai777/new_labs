import re
s='abb dfabbb abbbbb'
reg = re.compile('ab{2,3}')
result = reg.findall(s)
print(*result)