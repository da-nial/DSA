import sys

n, m, q = list(map(int, sys.stdin.readline().split()))

occupied = [[False for c in range(m)] for r in range(n)]
explored = [[False for c in range(m)] for r in range(n)]
layer = [[-1 for c in range(m)] for r in range(n)]

for r in range(n):
    line = list(sys.stdin.readline())
    for c in range(m):
        if line[c] == '*':
            occupied[r][c] = True

si, sj = list(map(int, sys.stdin.readline().split()))
si -= 1
sj -= 1

explored[si][sj] = True
layer[si][sj] = 0

bfs_queue = [(si, sj), ]
while bfs_queue:
    fi, fj = bfs_queue.pop(0)

    if fi > 0:
        if (not occupied[fi - 1][fj]) and (not explored[fi - 1][fj]):
            explored[fi - 1][fj] = True
            layer[fi - 1][fj] = layer[fi][fj] + 1
            bfs_queue.append((fi - 1, fj))
    if fi < n - 1:
        if (not occupied[fi + 1][fj]) and (not explored[fi + 1][fj]):
            explored[fi + 1][fj] = True
            layer[fi + 1][fj] = layer[fi][fj] + 1
            bfs_queue.append((fi + 1, fj))
    if fj > 0:
        if (not occupied[fi][fj - 1]) and (not explored[fi][fj - 1]):
            explored[fi][fj - 1] = True
            layer[fi][fj - 1] = layer[fi][fj] + 1
            bfs_queue.append((fi, fj-1))
    if fj < m - 1:
        if (not occupied[fi][fj + 1]) and (not explored[fi][fj + 1]):
            explored[fi][fj + 1] = True
            layer[fi][fj + 1] = layer[fi][fj] + 1
            bfs_queue.append((fi, fj + 1))


for _ in range(q):
    di, dj = list(map(int, sys.stdin.readline().split()))
    di -= 1
    dj -= 1
    print(layer[di][dj])
