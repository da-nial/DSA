n, k = list(map(int, input().split()))

rows = [n for _ in range(n)]
cols = [False for _ in range(n)]

answers = []

num_empty_cells = n * n
for _ in range(k):
    r, c = list(map(int, input().split()))
    r -= 1
    c -= 1

    if not cols[c]:
        for i in range(n):
            if rows[i] > 0:
                rows[i] -= 1
    cols[c] = True
    rows[r] = 0


    answer = sum(rows)
    answers.append(answer)

print(" ".join(list(map(str, answers))))
