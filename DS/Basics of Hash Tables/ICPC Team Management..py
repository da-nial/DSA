t = int(input())

for testcase in range(t):
    n, k = list(map(int, input().split()))

    _dict = {}
    for _ in range(n):
        name = input()
        _dict[len(name)] = _dict.get(len(name), 0) + 1

    # print(_dict)

    possible = True
    for length, count in _dict.items():
        if count % k != 0:
            possible = False
            break

    if possible:
        print("Possible")
    else:
        print("Not possible")
