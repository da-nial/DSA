from sys import stdin

# Farthest nodes in a tree


class Node:
    def __init__(self):
        self.dist = -1
        self.explored = False
        self.neighbors = []

    def get_child_weight(self, target_child):
        weight = None
        for child, weight in self.childs:
            if child == target_child:
                return weight

        # print("target child: " + str(target_child))
        # print("this node's children: " + str(self.childs))
        raise Exception

        return None


t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())

    nodes = []
    for _ in range(n):
        nodes.append(Node())

    for _ in range(n - 1):
        a, b, w = list(map(int, stdin.readline().split()))
        a = a - 1
        b = b - 1
        nodes[a].neighbors.append((b, w))
        nodes[b].neighbors.append((a, w))

    nodes[0].dist = 0
    nodes[0].explored = True
    bfs_queue = [0]

    farthest_leaf_dist = 0
    farthest_leaf = 0
    while bfs_queue:
        frontier = bfs_queue.pop(0)

        for neighbor, weight in nodes[frontier].neighbors:
            if not nodes[neighbor].explored:
                nodes[neighbor].explored = True
                nodes[neighbor].dist = nodes[frontier].dist + weight
                if nodes[neighbor].dist > farthest_leaf_dist:
                    farthest_leaf_dist = nodes[neighbor].dist
                    farthest_leaf = neighbor
                bfs_queue.append(neighbor)

    farthest_leaf_dist += 1

    for i in range(n):
        nodes[i].explored = False

    farthest_from_leaf_dist = 0
    farthest_from_leaf = 0
    nodes[farthest_leaf].dist = 0
    nodes[farthest_leaf].explored = True
    bfs_queue = [farthest_leaf]
    while bfs_queue:
        frontier = bfs_queue.pop(0)

        for neighbor, weight in nodes[frontier].neighbors:
            if not nodes[neighbor].explored:
                nodes[neighbor].explored = True
                bfs_queue.append(neighbor)
                nodes[neighbor].dist = nodes[frontier].dist + weight
                if nodes[neighbor].dist > farthest_from_leaf_dist:
                    farthest_from_leaf_dist = nodes[neighbor].dist
                    farthest_from_leaf = neighbor

    cost = 0
    if farthest_from_leaf_dist < 100:
        cost = 0
    elif farthest_from_leaf_dist < 1000:
        cost = 100
    elif farthest_from_leaf_dist < 10000:
        cost = 1000
    else:
        cost = 10000

    print("{} {}".format(cost, farthest_from_leaf_dist))
