from sys import stdin
import copy


class Node:
    def __init__(self, index):
        self.group = -1
        self.explored = False
        self.neighbors = []


def bfs(nodes, start_vertex, group):
    size = 1  # Size of the subgraph of start_vertex
    nodes[start_vertex].explored = True
    nodes[start_vertex].group = group
    bfs_queue = [start_vertex]
    while bfs_queue:
        frontier = bfs_queue.pop(0)
        for neighbor in nodes[frontier].neighbors:
            if not nodes[neighbor].explored:
                nodes[neighbor].explored = True
                nodes[neighbor].group = group
                size += 1
                bfs_queue.append(neighbor)

    return size


def is_connected(nodes, start_vertex, target_vertex):
    _nodes = copy.deepcopy(nodes)
    size = 1  # Size of the subgraph of start_vertex
    _nodes[start_vertex].explored = True
    bfs_queue = [start_vertex]
    while bfs_queue:
        frontier = bfs_queue.pop(0)
        for neighbor in _nodes[frontier].neighbors:
            if neighbor == target_vertex:
                return (True, size)

            if not _nodes[neighbor].explored:
                _nodes[neighbor].explored = True
                size += 1
                bfs_queue.append(neighbor)

    return (False, size)


n, m, p = list(map(int, stdin.readline().split()))
nodes = []


for i in range(n):
    nodes.append(Node(i))

conns = []
for _ in range(m):
    a, b = list(map(int, stdin.readline().split()))
    a -= 1
    b -= 1
    nodes[a].neighbors.append(b)
    nodes[b].neighbors.append(a)

    conns.append((a, b))


groups_size = []
group_id = 0
for i in range(n):
    if not nodes[i].explored:
        groups_size.append(bfs(nodes, i, group_id))
        group_id += 1

for i in range(n):
    nodes[i].explored = False

for i in range(n):
    nodes[i].explored = False

critical_edges = 0
i = 0
for conn in conns:
    a, b = conn
    nodes[a].neighbors.remove(b)
    nodes[b].neighbors.remove(a)

    size_ab = groups_size[nodes[a].group]
    # Check if the conn is critical
    connected, size_a = is_connected(nodes, a, b)
    if not connected:
        size_b = size_ab - size_a
        if abs(size_a - size_b) < p:
            critical_edges += 1

    nodes[a].neighbors.append(b)
    nodes[b].neighbors.append(a)

print(critical_edges)
