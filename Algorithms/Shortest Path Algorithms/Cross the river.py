import sys

t = int(sys.stdin.readline())

neighbors = []
for _ in range(t):
    n = int(sys.stdin.readline())

    for _ in range(n):
        x, y, r = list(map(int, sys.stdin.readline().split()))
    
    a, b = list(map(int, sys.stdin.readline()))
