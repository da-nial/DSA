import sys


class Node:
    def __init__(self):
        self.layer = -1
        self.occupied = False
        self.explored = False
        self.neighbors = []


n, m, q = list(map(int, sys.stdin.readline().split()))


def bfs(nodes, start_vertex):
    si, sj = start_vertex

    nodes[si][sj].explored = True
    nodes[si][sj].layer = 0

    bfs_queue = [(si, sj), ]
    while bfs_queue:
        fi, fj = bfs_queue.pop(0)

        for ni, nj in nodes[fi][fj].neighbors:
            if (not nodes[ni][nj].occupied) and (not nodes[ni][nj].explored):
                nodes[ni][nj].explored = True
                nodes[ni][nj].layer = nodes[fi][fj].layer + 1
                bfs_queue.append((ni, nj))


nodes = []
for r in range(n):
    line = []
    for c in range(m):
        line.append(Node())
    nodes.append(line)

for r in range(n):
    line = list(sys.stdin.readline())
    for c in range(m):
        if line[c] == '*':
            nodes[r][c].occupied = True

si, sj = list(map(int, sys.stdin.readline().split()))
si -= 1
sj -= 1

for r in range(n):
    for c in range(m):
        if r > 0:
            nodes[r][c].neighbors.append((r - 1, c))
        if r < n - 1:
            nodes[r][c].neighbors.append((r + 1, c))
        if c > 0:
            nodes[r][c].neighbors.append((r, c - 1))
        if c < m - 1:
            nodes[r][c].neighbors.append((r, c + 1))

bfs(nodes, (si, sj))


for _ in range(q):
    di, dj = list(map(int, sys.stdin.readline().split()))
    di -= 1
    dj -= 1
    print(nodes[di][dj].layer)
