N, M, T, C = list(map(int, input().split()))
conns = [[] for _ in range(N)]
explored = [False] * N
layer = [-1] * N
explored_by = [-1] * N  # Shows that each node was explored by who

for _ in range(M):
    U, V = list(map(int, input().split()))
    U = U - 1
    V = V - 1
    conns[U].append(V)
    conns[V].append(U)

for i in range(N):
    conns[i].sort()

X, Y = list(map(int, input().split()))
X = X - 1
Y = Y - 1

explored[X] = True
layer[X] = 0
bfs_queue = [X]

y_found = False
while (bfs_queue) and (not y_found):
    frontier = bfs_queue.pop(0)

    for neighbor in conns[frontier]:
        if not explored[neighbor]:
            explored_by[neighbor] = frontier

            bfs_queue.append(neighbor)
            explored[neighbor] = True
            layer[neighbor] = layer[frontier] + 1

            if neighbor == Y:
                y_found = True

K = layer[Y] + 1  # Number of cities to pass
print(K)

path = [Y]
iterator = Y
while iterator != X:
    iterator = explored_by[iterator]
    path.append(iterator)

path.reverse()
for i in range(len(path)):
    path[i] += 1
print(" ".join(map(str, path)))
