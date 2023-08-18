# FINAL SCORE: 100

class Node:
    def __init__(self):
        self.explored = False
        self.layer = -1
        self.conns = []


T = int(input())  # Number of Testcases

for i in range(T):
    N, M = list(map(int, input().split()))
    nodes = []
    for i in range(N):
        nodes.append(Node())

    for i in range(M):
        X, Y = list(map(int, input().split()))
        X = X - 1
        Y = Y - 1
        nodes[X].conns.append(Y)
        nodes[Y].conns.append(X)

    bfs_queue = [0]
    nodes[0].explored = True
    nodes[0].layer = 0
    while len(bfs_queue) != 0:
        frontier = bfs_queue.pop(0)  # dequeue

        for neighbor in nodes[frontier].conns:
            if not nodes[neighbor].explored:
                nodes[neighbor].explored = True
                nodes[neighbor].layer = nodes[frontier].layer + 1
                bfs_queue.append(neighbor)

    print(nodes[-1].layer)
