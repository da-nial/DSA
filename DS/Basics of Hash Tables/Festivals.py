t = int(input())

for testcase in range(t):
    n = int(input())

    _dict = {}
    for item in range(n):
        festival, amount = input().split()
        amount = int(amount)

        if festival not in _dict:
            _dict[festival] = [amount]
        elif len(_dict[festival]) < 3:
            _dict[festival].append(amount)
            _dict[festival].sort(reverse=True)
        else:
            if _dict[festival][0] < amount:
                _dict[festival].insert(0, amount)
                _dict[festival].pop()

            elif _dict[festival][1] < amount:
                _dict[festival].insert(1, amount)
                _dict[festival].pop()

            elif _dict[festival][2] < amount:
                _dict[festival].insert(2, amount)
                _dict[festival].pop()

    max_festival = None
    max_festival_amount = 0

    for festival, amounts in _dict.items():
        if sum(amounts) > max_festival_amount:
            max_festival = festival
            max_festival_amount = sum(amounts)

        if sum(amounts) == max_festival_amount:
            if festival < max_festival:
                max_festival = festival
                max_festival_amount = sum(amounts)

    print(f"{max_festival} {max_festival_amount}")
