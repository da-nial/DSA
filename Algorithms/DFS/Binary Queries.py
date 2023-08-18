n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        l = query[1] - 1
        r = query[2] - 1
        if arr[r]:
            print("ODD")
        else:
            print("EVEN")
    else:
        # x is the bit that should be flipped. (input indexing is 1 based, so we decrement it by 1.)
        x = query[1] - 1
        arr[x] = 1 - arr[x]
