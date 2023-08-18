t = int(input())

for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().split()))

    max_strength = max(strengths)

    strengths.sort()

    sum_abs_differences = 0
    i = 0
    while i < n - 1:
        sum_abs_differences += (i + 1) * (n - i - 1) * (strengths[i + 1] - strengths[i])
        i += 1

    print((sum_abs_differences * max_strength) % 1000000007)
