n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 0

i = 0
while i < n:
    count = 0

    j = i + 1
    while j < n and arr[j] == arr[i]:
        count += 1
        j += 1

    total += count
    i = j

print(total)
