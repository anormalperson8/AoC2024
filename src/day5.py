with open('../input/day5.txt', 'r') as f:
    s = f.read().strip()

# Example
# s = \
# """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.strip()

orders, updates = s.split("\n\n")
order_total = {} # Stores (k, list[v]), where k must be printed after any value v

for order in orders.splitlines():
    o = order.split("|")
    if int(o[1]) not in order_total.keys():
        order_total[int(o[1])] = [int(o[0])]
    else:
        order_total[int(o[1])].append(int(o[0]))

def check(l: list[int]) -> bool:
    for idx, u in enumerate(l):
        if u not in order_total.keys():
            continue
        for v in order_total[u]:
            if v in l[idx+1:]:
                return False
    return True

ret = []
incorrect = []
for update in updates.splitlines():
    update_order = list(map(int, update.split(",")))
    if check(update_order):
        ret.append(update_order[(len(update_order) - 1)//2])
    else:
        incorrect.append(update_order)

print("Part 1:", sum(ret))


def get_wrong(l: list[int]) -> tuple[int, int]:
    for idx, u in enumerate(l):
        if u not in order_total.keys():
            continue
        for v in order_total[u]:
            if v in l[idx+1:]:
                return idx, l.index(v)
    return len(l), len(l)

ret2 = []
for update in incorrect:
    ul = list(update)
    wrong_idx, to_swap = get_wrong(ul)
    while wrong_idx != len(ul):
        ul[wrong_idx], ul[to_swap] = ul[to_swap], ul[wrong_idx]
        wrong_idx, to_swap = get_wrong(ul)
    ret2.append(ul)

print("Part 2:", sum(list(map(lambda i: i[(len(i) - 1)//2], ret2))))
