t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr.sort()

    k = n - m

    min_sum = sum(arr[:k])
    max_sum = sum(arr[n-k:])

    print(max_sum - min_sum)
