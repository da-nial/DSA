class Node:
    def __init__(self):
        self.explored = False
        self.layer = -1
        self.conns = []

    def clear(self):
        self.explored = False
        self.layer = -1


def neighbors(src, dist):
    _nodes = nodes.copy()
    for node in _nodes:
        node.clear()

    _nodes[src].explored = True
    _nodes[src].layer = 0
    bfs_queue = [src]

    neighbors_in_dist = 0
    while bfs_queue:
        frontier = bfs_queue.pop(0)

        for neighbor in _nodes[frontier].conns:
            if not _nodes[neighbor].explored:
                _nodes[neighbor].explored = True
                _nodes[neighbor].layer = _nodes[frontier].layer + 1
                if _nodes[neighbor].layer == dist:
                    neighbors_in_dist += 1
                if _nodes[neighbor].layer > dist:
                    break
                bfs_queue.append(neighbor)

    print(neighbors_in_dist)


n, e = map(int, input().split())
nodes = []
for _ in range(n):
    nodes.append(Node())

for _ in range(e):
    u, v = map(int, input().split())
    nodes[u].conns.append(v)
    nodes[v].conns.append(u)

m = int(input())
for _ in range(m):
    src, dist = map(int, input().split())
    neighbors(src, dist)
