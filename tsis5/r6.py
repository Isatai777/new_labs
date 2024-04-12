import re
s='akskdjfb alskdbfj lKs. d d  hello_world'
reg = re.sub(r'[ ,.]', ':', s)
print(reg)
