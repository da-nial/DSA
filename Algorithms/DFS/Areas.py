import sys

sys.setrecursionlimit(10000)


def dfs(free, explored, start_vertex, area_size):
    r, c = len(explored), len(explored[0])
    si, sj = start_vertex
    explored[si][sj] = True

    if si > 0:
        ni, nj = (si - 1, sj)
        if (not explored[ni][nj]) and free[ni][nj]:
            area_size = dfs(free, explored, (ni, nj), area_size)
    if si < r - 1:
        ni, nj = (si + 1, sj)
        if (not explored[ni][nj]) and free[ni][nj]:
            area_size = dfs(free, explored, (ni, nj), area_size)
    if sj > 0:
        ni, nj = (si, sj - 1)
        if (not explored[ni][nj]) and free[ni][nj]:
            area_size = dfs(free, explored, (ni, nj), area_size)
    if sj < c - 1:
        ni, nj = (si, sj + 1)
        if (not explored[ni][nj]) and free[ni][nj]:
            area_size = dfs(free, explored, (ni, nj), area_size)

    return area_size + 1


t = int(input())  # Number of trials

for _ in range(t):
    r, c = list(map(int, sys.stdin.readline().split()))
    free = [[True for j in range(c)] for i in range(r)]
    explored = [[False for j in range(c)] for i in range(r)]

    for i in range(r):
        line = list(sys.stdin.readline())
        for j in range(c):
            if line[j] == '#':
                free[i][j] = False

    num_areas = 0
    area_sizes = []
    for i in range(r):
        for j in range(c):
            if (not explored[i][j]) and free[i][j]:
                num_areas += 1
                area_size = dfs(free, explored, (i, j), 0)
                area_sizes.append(area_size)

    print(num_areas)
    area_sizes_str = list(map(str, area_sizes))
    print(" ".join(area_sizes_str))
