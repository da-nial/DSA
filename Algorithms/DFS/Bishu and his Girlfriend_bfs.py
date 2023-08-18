class Node:
    def __init__(self):
        self.layer = -1
        self.explored = False
        self.has_girl = False
        self.childs = []


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


bfs_queue = [0]
nodes[0].layer = 0
nodes[0].explored = True

min_layer_with_girl = 100000
girls = []
exceeded = False
while bfs_queue and not exceeded:
    frontier = bfs_queue.pop(0)

    for child in nodes[frontier].childs:
        if not nodes[child].explored:
            nodes[child].explored = True
            nodes[child].layer = nodes[frontier].layer + 1
            bfs_queue.append(child)

            if nodes[child].layer > min_layer_with_girl:
                exceeded = True
                break

            if nodes[child].has_girl:
                girls.append(child)
                min_layer_with_girl = nodes[child].layer

print(str(min(girls) + 1))
