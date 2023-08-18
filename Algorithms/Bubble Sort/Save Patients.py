def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_elem_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_elem_idx]:
                min_elem_idx = j

        hold = arr[i]
        arr[i] = arr[min_elem_idx]
        arr[min_elem_idx] = hold


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        inserting_value = arr[i]

        j = i
        while arr[i] < arr[j - 1] and j > 0:
            j -= 1

        hold = arr[j]
        for k in range(j, i):
            new_hold = arr[k + 1]
            arr[k + 1] = hold
            hold = new_hold

        arr[j] = inserting_value


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(1, n):
            if arr[j] < arr[j - 1]:
                hold = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = hold

                swapped = True

        if not swapped:
            break


def merge_sort(arr):
    pass


def quick_sort(arr):
    pass


num_vaccines = int(input())

vaccine_midis = list(map(int, input().split()))
patient_midis = list(map(int, input().split()))

bubble_sort(vaccine_midis)
bubble_sort(patient_midis)

if any([patient_midis[i] >= vaccine_midis[i] for i in range(num_vaccines)]):
    print("No")
else:
    print("Yes")
