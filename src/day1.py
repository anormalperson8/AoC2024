from func_help.func_help import List
from collections import Counter

with open('../input/day1.txt', 'r') as f:
    s = f.read()

# Example
# s = \
# """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

left_original, right_original = zip(*List(s.splitlines()).stream().map(lambda x: (x[:x.index("   ")], x[x.index("   ") + 3:])).to_list())
sort_list = lambda l: List(l).stream().map(lambda i: int(i)).to_list().sort()
left, right = sort_list(left_original), sort_list(right_original)
print("Part 1:", List(zip(left, right)).stream().map(lambda i: abs(i[0] - i[1])).reduce(lambda a, b: a + b))

right_count = Counter(right_original)
print("Part 2:", List(left_original).stream().map(lambda i: int(i) * right_count[i] if i in right_count.keys() else 0).reduce(lambda a, b: a + b))



