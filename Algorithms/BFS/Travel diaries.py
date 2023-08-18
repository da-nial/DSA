from sys import stdin


def get_neighbors(matrix, i, j):
    n, m = len(matrix), len(matrix[0])

    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < n - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < m - 1:
        neighbors.append((i, j + 1))

    return neighbors


def main():
    n, m = list(map(int, stdin.readline().split()))

    matrix = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        matrix.append(row)

    bfs_queue = []

    batch = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                batch.append((i, j))

    bfs_queue.append(batch)

    time = 0
    while len(bfs_queue) != 0:
        batch = bfs_queue.pop(0)

        next_batch = []

        while len(batch) != 0:
            frontier = batch.pop(0)
            i, j = frontier

            neighbors = get_neighbors(matrix, i, j)
            for neighbor in neighbors:
                neighbor_i, neighbor_j = neighbor

                if matrix[neighbor_i][neighbor_j] == 1:
                    matrix[neighbor_i][neighbor_j] = 2
                    next_batch.append(neighbor)

        if next_batch:
            bfs_queue.append(next_batch)
            time += 1

    for i in range(n):
        if 1 in matrix[i]:
            print("-1")
            exit()

    print(time)


if __name__ == '__main__':
    main()
