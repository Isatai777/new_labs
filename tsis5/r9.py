import re
s = "HelloHowAreYou Good good"

reg = re.sub(r"(?<=\w)([A-Z])", r" \1",s)
print(reg)