def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i < len(left):
        arr[k:] = left[i:]
    elif j < len(right):
        arr[k:] = right[j:]

    return arr


def partition(arr, start, end):
    pivot_idx = start
    pivot = arr[pivot_idx]

    i = pivot_idx + 1
    j = i
    while j <= end:
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


def quick_sort(arr, start, end):
    if start > end:
        return

    pivot_idx = partition(arr, start, end)
    quick_sort(arr, start, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, end)

    return


# from random import sample
#
# arr = sample(range(0, 100), 100)
# print(arr)
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)
# exit()


N = 100000

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    hash_table = [[] for _ in range(N)]
    for __ in range(n):
        elem = int(input())
        hash_table[elem % N].append(elem)
        arr.append(elem)

    max_num_similars = 1
    for bucket in hash_table:
        if len(bucket) <= max_num_similars:
            continue

        # quick_sort(bucket, 0, len(bucket) - 1)
        bucket.sort()
        i = 0
        while i < len(bucket):
            num_similars = 0

            j = i
            while j < len(bucket) and bucket[j] == bucket[i]:
                j += 1
                num_similars += 1
            i = j
            if num_similars > max_num_similars:
                max_num_similars = num_similars

    print(max_num_similars)

    # # arr.sort()
    # # merge_sort(arr)
    # quick_sort(arr, 0, n - 1)
    # max_num_similars = 0
    # i = 0
    # while i < len(arr):
    #
    #     num_similars = 0
    #     j = i
    #     while j < len(arr) and arr[j] == arr[i]:
    #         j += 1
    #         num_similars += 1
    #
    #     i = j
    #     if num_similars > max_num_similars:
    #         max_num_similars = num_similars
    #
    # print(max_num_similars)
