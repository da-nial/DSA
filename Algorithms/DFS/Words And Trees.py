from sys import stdin, stdout


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.explored = False
        self.parent = -1
        self.childs = []


def _dfs(start_vertex):
    start_letter = nodes[start_vertex].letter
    found_letters[start_letter] = found_letters.get(start_letter, 0) + 1
    for child in nodes[start_vertex].childs:
        if not nodes[child].explored:
            nodes[child].explored = True
            _dfs(child)


n, q = list(map(int, stdin.readline().split()))
nodes = []
letters = stdin.readline().split()
for letter in letters:
    nodes.append(Node(letter))

nodes[0].parent = 0
for _ in range(n - 1):
    u, v = list(map(int, stdin.readline().split()))
    u = u - 1
    v = v - 1
    if nodes[u].parent == -1:
        nodes[u].parent = v
        nodes[v].childs.append(u)
    else:
        nodes[v].parent = u
        nodes[u].childs.append(v)

# for i in range(n):
#     print("{} childs: {}".format(i + 1, nodes[i].childs))
# print("\n\n\n")
found_letters = {}

for _ in range(q):
    start_vertex, string = stdin.readline().split()
    start_vertex = int(start_vertex)
    start_vertex = start_vertex - 1
    found_letters = {}
    letters_needed = 0
    nodes[start_vertex].explored = True
    _dfs(start_vertex)
    # print(found_letters)
    for letter in string:
        if (letter in found_letters) and (found_letters[letter] > 0):
            found_letters[letter] -= 1
        else:
            letters_needed += 1

    for i in range(n):
        nodes[i].explored = False

    print(letters_needed)
