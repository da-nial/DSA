def get_parent(i):
    if i == 0:
        return None

    return (i + 1) // 2 - 1


def get_children(i):
    return 2 * i + 1, 2 * i + 2


class Heap:
    def __init__(self, arr=[]):
        self.arr = arr

    def insert(self, value):
        self.arr.append(value)

        i = len(self.arr) - 1
        self.bubble_up(i)

    def bubble_up(self, i):
        parent_i = get_parent(i)
        while parent_i is not None and self.arr[i] < self.arr[parent_i]:
            hold = self.arr[i]
            self.arr[i] = self.arr[parent_i]
            self.arr[parent_i] = hold

            i = parent_i
            parent_i = get_parent(i)

    def extract_min(self):
        min_value = self.arr.pop(0)

        last_leaf = self.arr.pop(-1)
        self.arr.insert(0, last_leaf)
        self.bubble_down(0)

        return min_value

    def bubble_down(self, i):
        left, right = get_children(i)

        while left < len(self.arr) and right < len(self.arr):
            if self.arr[i] < self.arr[left] and self.arr[i] < self.arr[right]:
                return

            elif self.arr[left] < self.arr[right]:
                hold = self.arr[i]
                self.arr[i] = self.arr[left]
                self.arr[left] = hold

                i = left

            elif self.arr[right] < self.arr[left]:
                hold = self.arr[i]
                self.arr[i] = self.arr[right]
                self.arr[right] = hold

                i = right

            left, right = get_children(i)

        if left < len(self.arr) and self.arr[left] < self.arr[i]:
            hold = self.arr[i]
            self.arr[i] = self.arr[left]
            self.arr[left] = hold

        return

    def visualize(self):
        if len(self.arr) == 0:
            return

        print([self.arr[0]])

        i = 1
        while i < len(self.arr):
            print(self.arr[i:2 * i + 1])
            i = i * 2 + 1
