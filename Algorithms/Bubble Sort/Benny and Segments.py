def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            arr[k] = left[i]
            i += 1
        elif left[i][0] > right[j][0]:
            arr[k] = right[j]
            j += 1

        elif left[i][0] == right[j][0]:
            if left[i][1] < right[j][1]:
                arr[k] = left[i]
                i += 1
            elif left[i][1] > right[j][1]:
                arr[k] = right[j]
                j += 1

        k += 1

    if i < len(left):
        arr[k:] = left[i:]
    elif j < len(right):
        arr[k:] = right[j:]

    return arr


def find_path(arr, i, current_l, target_l):
    # print(f"called find_path with i: {i}, current_l: {current_l}")

    j = i + 1
    while j < len(arr) and arr[j][0] <= arr[i][1]:
        if arr[j][1] < arr[i][1]:
            j += 1
            continue
        added_l = arr[j][1] - arr[i][1]
        remaining_l = target_l - (current_l + added_l)

        # print("\n")
        # print(f"arr: {arr}")
        # print(f"i: {i}")
        # print(f"testing j: {j}")
        # print(f"target_l: {target_l}")
        # print(f"current_l: {current_l}")
        # print(f"added_l: {added_l}")
        # print(f"remaining_l: {remaining_l}")

        if remaining_l == 0:
            return [arr[j], ]
        elif remaining_l < 0:
            # print("exceeded, go to next j")
            j += 1
            continue
        elif remaining_l > 0:
            remaining_path = find_path(arr, j, current_l + added_l, target_l)
            if remaining_path is not None:
                return [arr[j]] + remaining_path
            else:
                j += 1
                continue

    return None


t = int(input())

for _ in range(t):
    n, l = list(map(int, input().split()))

    roads = []
    for i in range(n):
        start, end = list(map(int, input().split()))
        roads.append((start, end))

    merge_sort(roads)

    found = False
    for i in range(n):
        if roads[i][1] - roads[i][0] == l:
            # print(roads[i])
            print("Yes")
            found = True
            break

        found_path = find_path(roads, i, roads[i][1] - roads[i][0], l)

        if found_path is not None:
            path = [roads[i]] + found_path
            # print(i)
            # print(roads[i])
            # print(found_path)
            print("Yes")
            found = True
            break

    if not found:
        print("No")
