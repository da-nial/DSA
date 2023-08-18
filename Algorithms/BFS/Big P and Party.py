import sys


a, b = list(map(int, sys.stdin.readline().split()))

conns = [[] for _ in range(b)]
explored = [False] * a
layer = [-1] * a

for _ in range(b):
    u, v = list(map(int, sys.stdin.readline().split()))
    conns[u].append(v)
    conns[v].append(u)


layer[0] = 0
explored[0] = True
bfs_queue = [0]

while bfs_queue:
    frontier = bfs_queue.pop(0)

    for neighbor in conns[frontier]:
        if not explored[neighbor]:
            explored[neighbor] = True
            layer[neighbor] = layer[frontier] + 1
            bfs_queue.append(neighbor)

for i in range(a)[1::]:
    print(layer[i])
