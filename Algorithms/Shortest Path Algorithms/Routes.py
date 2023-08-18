import sys


k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
x = int(sys.stdin.readline())

conns = [[] for _ in range(n)]

for _ in range(x):
    s, d, t, c = list(map(int, sys.stdin.readline().split()))
    s -= 1
    d -= 1

    conns[s].append((d, t, c))
    conns[d].append((s, t, c))

s = int(sys.stdin.readline())
s -= 1
d = int(sys.stdin.readline())
d -= 1


X = [s]

A = [1000000] * n
A[s] = 0

B = [[] for _ in range(n)]
B[s] = [s]
C = []
for neighbor, time, cost in conns[s]:
    C.append((s, neighbor, 0 + k * time + cost))

while len(X) < n:
    winner = -1
    winner_source = -1
    winner_dscore = 1000000
    for source, candidate, dscore in C:
        if dscore < winner_dscore:
            winner_source = source
            winner = candidate
            winner_dscore = dscore

    X.append(winner)
    A[winner] = winner_dscore
    B[winner] = B[source] + [winner]

    for neighbor, time, cost in conns[winner]:
        C.append((winner, neighbor, 0 + k * time + cost))

    C = [(source, neighbor, dscore) for (source, neighbor, dscore) in C if not (neighbor in X)]

    if d in X:
        break


print("Shortest path distance: {}".format(A[d]))
print("Shortest path: {}".format(B[d]))
