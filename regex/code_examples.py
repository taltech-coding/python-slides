import re

match = re.search("abc", "aabca")
print(match.group())  # abc is found in text
match = re.search("xyz", "aabca")
print(match is None)  # no match

import re

text = "backslash: \\"
print(text)  # backslash: \
print("match" if re.search("\\\\", text) else "no match")
print("match" if re.search(r"\\", text) else "no match")
# print("match" if re.search("\\", text) else "no match")

print("match" if re.search("(.)\1", "aa") else "no match")
print("match" if re.search("(.)\\1", "aa") else "no match")
print("match" if re.search(r"(.)\1", "aa") else "no match")


import re

match = re.search("xk(ab)?(cd)", "xkcde")
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))


import re

match = re.search("(?:ab)?(cd)e", "acde")
print(match.group())
print(match.groups())

match = re.search("(ab)?(cd)e", "acde")
print(match.group())
print(match.groups())

import re

m1 = re.match("c", "abcdef")
m2 = re.search("c", "abcdef")

print("Match" if m1 is not None else "No match")
print("Match" if m2 is not None else "No match")

import re
text= "tere minu@email.ee, sõbra email on guido@baggins.com ja guits@bag.com"

emails= re.findall(r"[\w.-]+@[\w.-]+", text)
for email in emails:
    print(email)

for email in re.finditer(r"[\w.-]+@[\w.-]+", text):
    print(email.group())
