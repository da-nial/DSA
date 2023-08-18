"""
The solution below passed all test cases except one
As I can't think of any other solution with less time complexity, I think the problem
is with Python speed itself. Maybe the algorithm implemented here works for c++, I don't know.
"""

n = int(input())

arr = list(map(int, input().split()))

_dict2 = {}
for idx, elem in enumerate(arr):
    j = idx + 1
    key = elem - (j * j)
    if _dict2.get(key) is None:
        _dict2[key] = [j]
    else:
        _dict2[key].append(j)

# print(_dict2)

num_answers = 0
for idx, elem in enumerate(arr):
    i = idx + 1
    key = elem + (i * i)

    if _dict2.get(key) is not None:
        for j in _dict2[key]:
            num_answers += 1

print(num_answers)
