import re

text = """re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
re.fullmatch("r.*n", "python") # No match
"""

# pattern = re.compile(r'(?P<grupa1><.+>)')
# print(type(pattern))
#
# search_patterns = pattern.search(text)
# print(search_patterns.group('grupa1'))
#
# pattern = re.compile(r'(?P<grupa1>re.*)')
# match_patterns = pattern.match(text)
# print(match_patterns.group('grupa1'))
#
#
# all_found_patterns = pattern.findall(text)
# print(all_found_patterns)
#
# all_found_patterns = re.findall(r'.*Match.*', text)
# print(all_found_patterns)
#
# # search for digits separated by comma
# result = re.search(r'\(\d, \d\)', text)
# print(result.group(0))
#
# result = re.findall(r'\(\d, \d\)', text)
# print(result)

# run cli command

import os

result = os.popen("ipconfig")
print(result.read())
