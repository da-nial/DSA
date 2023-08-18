class Node:
    def __init__(self):
        self.explored = False
        self.layer = -1
        self.childs = []
        self.has_girl = False


N = int(input())
nodes = []

for _ in range(N):
    nodes.append(Node())

for _ in range(N - 1):
    u, v = list(map(int, input().split()))
    u = u - 1
    v = v - 1
    _max = max(u, v)
    _min = min(u, v)
    nodes[_min].childs.append(_max)


Q = int(input())
for _ in range(Q):
    girl_country = int(input())
    girl_country = girl_country - 1
    nodes[girl_country].has_girl = True

girls = []


def _dfs(start_vertex):
    for child in nodes[start_vertex].childs:
        if not nodes[child].explored:
            if nodes[child].has_girl:
                girls.append(child)
                break
            _dfs(child)


_dfs(0)
print(str(min(girls) + 1))
