text = """
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
"""

from collections import Counter, deque

c = Counter(text)
print(c)  # count letters

c = Counter(text.split())
print(c)  # count words

c["new"] += 3  # increment any counter
print(f'Modified Counter {c}')

# fixed length queue
d = deque(maxlen=5)
d.append(1)
for i in "text":
    d.append(i)
print(d)
d.append(3)
print(d)
d.pop()
print(d)