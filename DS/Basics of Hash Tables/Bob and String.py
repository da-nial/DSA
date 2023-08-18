num_testcases = int(input())

for testcase in range(num_testcases):
    s = input()
    t = input()

    hash_t1 = [0 for _ in range(256)]
    hash_t2 = [0 for _ in range(256)]

    for char in s:
        idx = ord(char)
        hash_t1[idx] += 1

    for char in t:
        idx = ord(char)
        hash_t2[idx] += 1

    num_ops = 0
    for idx in range(len(hash_t1)):
        num_ops += abs(hash_t1[idx] - hash_t2[idx])

    print(num_ops)
