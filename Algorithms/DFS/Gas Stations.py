n, x = list(map(int, input().split()))

p = list(map(int, input().split()))

fuel = x
result = 0
while fuel > 0:
    fuel -= p[result]
    result += 1

    if result == n - 1:
        break

print(result)
