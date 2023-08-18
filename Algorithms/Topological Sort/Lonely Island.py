import sys

# Memory limit exceeded! maybe using a dictionary instead of 2d list helps?


def dfs(explored, outgoing_v, start_vertex, sink_fr):
    if not outgoing_v[start_vertex]:
        sink_fr[start_vertex][start_vertex] = sink_fr[start_vertex].get(
            start_vertex, 0) + 1
    else:
        for neighbor in outgoing_v[start_vertex]:
            if not explored[neighbor]:
                dfs(explored, outgoing_v, neighbor, sink_fr)

            sink_fr[start_vertex] = {x: sink_fr[start_vertex].get(x, 0) + sink_fr[neighbor].get(x, 0)
                                     for x in set(sink_fr[start_vertex]).union(sink_fr[neighbor])
                                     }

    print("node_i {} done!".format(start_vertex))
    explored[start_vertex] = True


n, m, r = list(map(int, sys.stdin.readline().split()))
outgoing_v = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    u -= 1
    v -= 1
    outgoing_v[u].append(v)


sink_fr = [{} for i in range(n)]
explored = [False for _ in range(n)]

for node_i in range(n):
    if not explored[node_i]:
        dfs(explored, outgoing_v, node_i, sink_fr)

ultimate_fr = {}
for start_vertex in range(n):
    ultimate_fr = {x: ultimate_fr.get(x, 0) + sink_fr[start_vertex].get(x, 0)
                   for x in set(ultimate_fr).union(sink_fr[start_vertex])
                   }

print(max(ultimate_fr, key=ultimate_fr.get) + 1)
