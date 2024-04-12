import re
s='akskdjf alskdfj lks d d  hello_world akfjajfajg_adsfs'
reg = re.compile('[a-z]+_[a-z]+')
result = reg.findall(s)
print(result)