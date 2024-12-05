import re
from func_help.func_help import List

with open('../input/day3.txt', 'r') as f:
    s = f.read()

# Examples
# s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

mul_to_val = lambda x: x.stream().map(lambda i: (i[4:i.index(",")], i[i.index(",") + 1:-1])).map(lambda i: int(i[0]) * int(i[1])).reduce(lambda i, j: i + j)
print("Part 1:", mul_to_val(List(re.findall("mul\([0-9]+,[0-9]+\)", s))))

l2 = List(re.findall("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", s)).stream().map(lambda i: list(filter(lambda x: x != "", i))[0]).to_list()
do = l2.stream().filter(lambda i: i == "do()").to_list()
do_not = l2.stream().filter(lambda i: i == "don't()").to_list()

l2_new = List(l2)
for i in range(len(do)):
    if "don't()" in l2_new:
        idx1 = l2_new.index("don't()")
        idx2 = l2_new.index("do()")
        if idx1 < idx2:
            l2_new = List(l2_new[:idx1]).extend_and_ret(l2_new[idx2 + 1:])
        else:
            l2_new.remove("do()")
    else:
        l2_new.remove("do()")


print("Part 2:", mul_to_val(l2_new))

# stat = True
# total = 0
# for i in l2:
#     stat = False if i == "don't()" else True if i == "do()" else stat
#     if stat and i != "do()":
#         total += int(i[4:i.index(",")]) * int(i[i.index(",") + 1:-1])
# print(total)
