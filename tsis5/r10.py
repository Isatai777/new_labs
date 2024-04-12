import re

def camel_to_snake(s: str):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).lower()

print(camel_to_snake("HelloHowAreYou"))