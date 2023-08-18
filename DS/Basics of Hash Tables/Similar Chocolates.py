
MAX_A = 1000000 + 1
arr = [0 for _ in range(MAX_A)]

for i in range(MAX_A):
    for j in range(i, MAX_A):
        pass



def count_divisors(num):
    count = 0
    for i in range(1, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2

    return count


n = int(input())

arr = list(map(int, input().split()))

_dict = {}
for elem in arr:
    key = count_divisors(elem)

    if _dict.get(key) is None:
        _dict[key] = [elem]
    else:
        _dict[key].append(elem)

num_pairs = 0
for key, value in _dict.items():
    n = len(value)
    num_pairs += (n * (n - 1)) // 2

print(num_pairs)
