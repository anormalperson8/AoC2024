import re
from func_help.func_help import List

with open('../input/day4.txt', 'r') as f:
    s = f.read().strip()


# Example
# s = \
# """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.strip()

horizontal = List(s.splitlines()).stream().to_list()
horizontal_backwards = horizontal.stream().map(lambda i: i[::-1]).to_list()

vertical = List(zip(*horizontal)).stream().map(lambda i: "".join(i)).to_list()
vertical_backwards = vertical.stream().map(lambda i: i[::-1]).to_list()

diagonal = (List(["".join([horizontal[i+j][j] for j in range(len(horizontal[0]) - i)]) for i in range(len(vertical[0]))][:0:-1])
            .extend_and_ret(List(["".join([horizontal[j][i+j] for j in range(len(vertical[0]) - i)]) for i in range(len(horizontal[0]))]))
            )
diagonal_backwards = diagonal.stream().map(lambda i: i[::-1]).to_list()

reverse_diagonal = (List(["".join([horizontal[i+j][len(horizontal[0])-j-1] for j in range(len(horizontal[0]) - i)]) for i in range(len(vertical[0]))][:0:-1])
                    .extend_and_ret(List(["".join([horizontal[j][len(horizontal[0])-i-j-1] for j in range(len(vertical[0]) - i)]) for i in range(len(horizontal[0]))])))
reverse_diagonal_backwards = reverse_diagonal.stream().map(lambda i: i[::-1]).to_list()

toFind = "(XMAS)"
all_combinations = List([horizontal, horizontal_backwards, vertical, vertical_backwards, diagonal, diagonal_backwards, reverse_diagonal, reverse_diagonal_backwards])
v = all_combinations.stream().map(lambda i: i.stream().map(lambda j: len(re.findall(toFind, j))).reduce(lambda x, y: x + y)).reduce(lambda x, y: x + y)
print("Part 1:", v)

# So I gave up doing it in a smart way
def check(letter: list[str]) -> bool:
    diagonal1 = letter[0] + letter[2] + letter[4]
    diagonal2 = letter[1] + letter[2] + letter[3]
    return (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM")

num = 0
for i in range(len(horizontal[0]) - 2):
    for j in range(len(horizontal[0]) - 2):
        num += check([horizontal[i][j], horizontal[i][j+2], horizontal[i+1][j+1], horizontal[i+2][j], horizontal[i+2][j+2]])

print("Part 2:", num)






