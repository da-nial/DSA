from sys import stdin


def dfs_t(explored, outgoing_v, f_times, start_vertex):
    explored[start_vertex] = True

    for neighbor in outgoing_v[start_vertex]:
        if not explored[neighbor]:
            dfs_t(explored, outgoing_v, f_times, neighbor)

    f_times.append(start_vertex)


def dfs_s(explored, outgoing_v, leaders, start_vertex):
    explored[start_vertex] = True

    for neighbor in outgoing_v[start_vertex]:
        if not explored[neighbor]:
            leaders[neighbor] = leaders[start_vertex]
            dfs_s(explored, outgoing_v, leaders, neighbor)


n, m = list(map(int, stdin.readline().split()))

outgoing_v = [[] for _ in range(n)]
outgoing_v_rev = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, stdin.readline().split()))
    u -= 1
    v -= 1
    outgoing_v[u].append(v)
    outgoing_v_rev[v].append(u)

f_times = []
explored = [False for _ in range(n)]
for i in range(n):
    if not explored[i]:
        dfs_t(explored, outgoing_v_rev, f_times, i)

explored = [False for _ in range(n)]
leaders = [-1 for _ in range(n)]
for node in f_times:
    if not explored[node]:
        leaders[node] = node
        dfs_s(explored, outgoing_v, leaders, node)


is_special = []
for i in range(n):
    if leaders[i] != i:
        is_special.append('1')
    else:
        for neighbor in outgoing_v[i]:
            if leaders[neighbor] == i:
                is_special.append('1')
            else:
                is_special.append('0')

print(' '.join(is_special))
