n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

count = [0 for _ in range(1000000)]

for num in arr:
    if k - num < len(arr):
        if count[k - num]:
            print("YES")
            exit()

    count[num] += 1

print("NO")
