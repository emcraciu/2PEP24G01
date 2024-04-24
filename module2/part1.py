import re

"""
re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match
<re.Match object; span=(2, 3), match='c'>
re.fullmatch("p.*n", "python") # Match
<re.Match object; span=(0, 6), match='python'>
re.fullmatch("r.*n", "python") # No match
"""

re.compile()