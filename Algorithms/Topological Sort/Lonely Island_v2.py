from sys import stdin


n, m, r = list(map(int, stdin.readline().split()))
r -= 1

incomings = [[] for _ in range(n)]
outgoings = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, stdin.readline().split()))
    u -= 1
    v -= 1
    incomings[v].append(u)
    outgoings[u].append(v)

sink_nodes = []
explored = [False for _ in range(n)]
probs = [0.0 for _ in range(n)]


probs[0] = 1
explored[0] = True
bfs_queue = [0]

while bfs_queue:
    frontier = bfs_queue.pop(0)

    for incoming_neighbor in incomings[frontier]:
        deg_incoming_neighbor = len(outgoings[incoming_neighbor])
        probs[frontier] += probs[incoming_neighbor] / deg_incoming_neighbor

    if outgoings[frontier]:
        for outgoing_neighbor in outgoings[frontier]:
            if not explored[outgoing_neighbor]:
                explored[outgoing_neighbor] = True
                bfs_queue.append(outgoing_neighbor)
    else:
        sink_nodes.append(frontier)

sink_nodes_probs = [(sink_node, probs[sink_node]) for sink_node in sink_nodes]
sink_nodes_probs.sort(key=lambda x: x[1])

most_probable_sinks = [sink_nodes_probs[-1][0] + 1]
max_prob = sink_nodes_probs[-1][1]

for i in range(len(sink_nodes) - 2, -1, -1):
    this_sink = sink_nodes_probs[i]
    if max_prob - this_sink[1] < 10 ** -9:
        most_probable_sinks.append(this_sink[0] + 1)
    else:
        break

most_probable_sinks = list(map(str, most_probable_sinks))
print(" ".join(most_probable_sinks))
