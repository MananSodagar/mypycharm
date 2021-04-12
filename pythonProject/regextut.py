import re
pattern = r"Cookie"
sequence = "Cookie"
print(re.match(pattern, sequence))

# x=re.search(r'hi',"hello hi miami")
# y=re.search(r'doba$','adoba adoba')
# print(y)

#
# print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())
#
# ## Matches any character except single letter, digit or underscore
# print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())
#
# ## Uppercase W won't match single letter, digit
# print("Uppercase W won't match, and return:", re.search(r'Co\Wk\We', 'Cookie'))

# print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())

# print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())
# print("Uppercase S:", re.search(r'cook\Se', "cook'e").group())
# print("Lowercase w:", re.search(r'Cook\We', 'Cook"e').group())

"""
\t - Lowercase t. Matches tab.
\n - Lowercase n. Matches newline.
\r - Lowercase r. Matches return.
\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
\Z - Uppercase z. Matches only at the end of the string.

TIP: ^ and \A are effectively the same, and so are $ and \Z. Except when dealing with MULTILINE mode. Learn more about it in the flags section.
"""

# \b - Lowercase b. Matches only the beginning or end of the word.
#
# # Example for \t
# print("\\t (TAB) example: ", re.search(r'Eat\tcake', 'Eat    cake').group())
#
# # Example for \b
# print("\\b match gives: ",re.search(r'\b[A-E]ookie', 'Cookie').group())

# * - Checks if the preceding character appears zero or more times starting from that position.
#
# # Checks for any occurrence of a or o or both in the given sequence
# re.search(r'Ca*o*kie', 'Cookie').group()
# 'Cookie'
# ? - Checks if the preceding character appears exactly zero or one time starting from that position.
#
# # Checks for exactly zero or one occurrence of a or o or both in the given sequence
# re.search(r'Colou?r', 'Color').group()
# 'Color'

#
# {x} - Repeat exactly x number of times.
# {x,} - Repeat at least x times or more.
# {x, y} - Repeat at least x times but no more than y times.
#
# re.search(r'\d{9,10}', '0987654321').group()


# x=re.search(r'1+$', '00000098765432111111').group()
# print(x)

# iiiiiiiiiiiimmmmmmmmmmmmpppppppppppp

statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.]+)@([\w\.]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)