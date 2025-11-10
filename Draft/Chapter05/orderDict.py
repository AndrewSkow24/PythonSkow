quotes = {"Moe": "A wise guy, huh ?", "Larry": "Ow!", "Curly": "Nyuk, nyuk!"}

for stooge in quotes:
    print(stooge)

from collections import OrderedDict

quotes = OrderedDict(
    [("Moe", "A wise guy, huh"), ("Larry", "Ow!"), ("Curly", "Nuyk, Nyuk!")]
)

for stooge in quotes:
    print(stooge)

from pprint import pprint

print(quotes)
pprint(quotes)
