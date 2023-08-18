import sys


def dfs(path, explored, start_vertext, cur_distance):
    pass


n = int(sys.stdin.readline())
path = [[False for j in range(n)] for i in range(n)]
explored = [[False for j in range(n)] for i in range(n)]
layer = [[-1 for j in range(n)] for i in range(n)]

si, sj = -1, -1
ei, ej = -1, -1
for i in range(n):
    line = sys.stdin.readline().split()
    for j in range(n):
        if line[j] == 'S':
            si, sj = i, j
            path[i][j] = True
        elif line[j] == 'E':
            ei, ej = i, j
            path[i][j] = True
        elif line[j] == 'P':
            path[i][j] = True


explored[si][sj] = True
layer[si][sj] = 0

bfs_queue = [(si, sj)]
while bfs_queue:
    frontier = bfs_queue.pop(0)
    fi, fj = frontier

    if fi == ei and fj == ej:
        break

    if fi > 0:
        ni, nj = fi - 1, fj
        if path[ni][nj] and (not explored[ni][nj]):
            explored[ni][nj] = True
            layer[ni][nj] = layer[fi][fj] + 1
            bfs_queue.append((ni, nj))

    if fi < n - 1:
        ni, nj = fi + 1, fj
        if path[ni][nj] and (not explored[ni][nj]):
            explored[ni][nj] = True
            layer[ni][nj] = layer[fi][fj] + 1
            bfs_queue.append((ni, nj))

    if fj > 0:
        ni, nj = fi, fj - 1
        if path[ni][nj] and (not explored[ni][nj]):
            explored[ni][nj] = True
            layer[ni][nj] = layer[fi][fj] + 1
            bfs_queue.append((ni, nj))

    if fj < n - 1:
        ni, nj = fi, fj + 1
        if path[ni][nj] and (not explored[ni][nj]):
            explored[ni][nj] = True
            layer[ni][nj] = layer[fi][fj] + 1
            bfs_queue.append((ni, nj))


print(layer[ei][ej])
