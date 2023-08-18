def partition(arr, start, end):
    pivot_idx = start
    pivot = arr[pivot_idx]

    i = pivot_idx + 1
    j = i
    while j < end:
        if arr[j] < pivot:
            hold = arr[j]
            arr[j] = arr[i]
            arr[i] = hold

            i += 1

        j += 1

    hold = arr[i - 1]
    arr[i - 1] = arr[pivot_idx]
    arr[pivot_idx] = hold

    return i - 1


def i_order_statistic(arr, start, end, i):
    pivot = arr[start]

    pivot_idx = partition(arr, start, end)

    if pivot_idx == i:
        return arr[i]
    elif pivot_idx < i:
        pass
    else:
        pass


t = int(input())

for _ in range(t):
    n = int(input())

    houses = []
    for i in range(n):
        house_i = list(map(int, input().split()))
        houses.append(house_i)
