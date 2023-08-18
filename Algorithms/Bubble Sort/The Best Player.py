def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            arr[k] = left[i]
            i += 1
        elif left[i][1] > right[j][1]:
            arr[k] = right[j]
            j += 1

        else:
            if left[i][0] > right[j][0]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

        k += 1

    if i != len(left):
        arr[k:] = left[i:]

    elif j != len(right):
        arr[k:] = right[j:]

    return arr


n, t = list(map(int, input().split()))

fans = []
for _ in range(n):
    name, quotient = input().split()
    quotient = int(quotient)

    fans.append((name, quotient))

fans = merge_sort(fans)
# print(fans)

for i in range(n - 1, n - 1 - t, -1):
    print(fans[i][0])
