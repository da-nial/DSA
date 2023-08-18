n, m = list(map(int, input().split()))

matrix = [[None for col in range(m)] for row in range(n)]

_dict = {}
for row in range(n):
    y_s = list(map(int, input().split()))

    for col, y in enumerate(y_s):
        _dict[y] = (row, col)

q = int(input())

for _ in range(q):
    query = int(input())

    answer = _dict.get(query, (-1, -1))
    print(" ".join(list(map(str, answer))))
