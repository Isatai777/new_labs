import re
s = 'ajhfahfahpfhasfhjahkfabb ahfjahfajshfdj ab'
reg = re.compile('a.*b')
result = reg.findall(s)
print(result)
