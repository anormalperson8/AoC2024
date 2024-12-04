from func_help.func_help import List
from itertools import chain, combinations

def check_line(line: "List[int]") -> bool:
    if len(line.to_set()) != len(line) or (line.sort() != line and line.sort(lambda a, b: b - a) != line):
        return False
    def check(line_inner: "List[int]", increase: bool) -> bool:
        if len(line_inner) == 1:
            return True
        if abs(line_inner[0] - line_inner[1]) > 3:
            return False
        if (increase and line_inner[0] < line_inner[1]) or (not increase and line_inner[0] > line_inner[1]):
            return check(line_inner[1:], increase)
        return False
    return check(line, line[0] < line[1])

def check_line2(line: "List[int]"):
    return List([line]).extend_and_ret(List(chain(combinations(line, len(line) - 1))).stream().map(lambda i: List(i)).to_list()).stream().map(lambda l: check_line(l)).reduce(lambda a, b: a or b)


with open('../input/day2.txt', 'r') as f:
    s = f.read()

# Example
# s = \
# """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

lines = List(s.splitlines()).stream().map(lambda r: List(r.split(" ")).stream().map(lambda i: int(i)).to_list()).to_list()
print("Part 1:", lines.stream().map(check_line).reduce(lambda a, b: a + b))
print("Part 2:", lines.stream().map(check_line2).reduce(lambda a, b: a + b))
