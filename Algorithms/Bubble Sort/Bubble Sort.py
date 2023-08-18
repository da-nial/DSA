n = int(input())

arr = list(map(int, input().split()))


def bubble_sort(arr):
    count = 0
    n = len(arr)

    swapped = True
    while swapped:
        swapped = False
        count += 1

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                hold = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = hold
                swapped = True
    return count


print(bubble_sort(arr))
