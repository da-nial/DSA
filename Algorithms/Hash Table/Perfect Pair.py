from sys import stdin


def h(key):
    return key % 11


t = int(stdin.readline())

num_buckets = 13
buckets = [[] for _ in range(num_buckets)]
for _ in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))

    for i in range(n):
        pos = h(i)
        arr[pos].append(i)
        
