import re
s = 'AHFBDSHSBJDFHDSFBbsbfbskbdf sdfbsfbABSBFB sbfskf'
reg = re.compile('[A-Z]+[a-z]+')
result = reg.findall(s)
print(result)