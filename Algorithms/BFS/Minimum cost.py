import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    p = [pi - 1 for pi in p]

    explored = [False] * n
    layer = [i for i in range(n)]

    for source in range(n):
        if not explored[source]:
            explored[source] = True

            bfs_queue = [source]

            while (bfs_queue):
                frontier = bfs_queue.pop(0)
                explored[frontier] = True

                path = [frontier]
                neighbor = p[frontier]
                while (p[neighbor] != neighbor) and (not explored[neighbor]):
                    explored[neighbor] = True
                    layer[neighbor] = layer[frontier]
                    path.append(neighbor)

                    neighbor = p[neighbor]

                for node in path:
                    if node > 1:
                        if not explored[node - 1]:
                            if layer[node] + 1 < layer[node - 1]:
                                layer[node - 1] = layer[node] + 1
                            bfs_queue.append(node - 1)

                    if node < n - 1:
                        if not explored[node + 1]:
                            if layer[node] + 1 < layer[node + 1]:
                                layer[node + 1] = layer[node] + 1
                            bfs_queue.append(node + 1)

    print(layer[n - 1])
