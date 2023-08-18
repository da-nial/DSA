t = int(input())

for _ in range(t):
    n = int(input())
    girls = []

    max_score = None
    second_max_score = None
    total_sadness = 0
    for __ in range(n):
        happiness, sadness = list(map(int, input().split()))

        score = happiness + sadness
        if max_score is None or score > max_score:
            second_max_score = max_score
            max_score = score
        elif second_max_score is None or score > second_max_score:
            second_max_score = score

        total_sadness += sadness
        girls.append((happiness, sadness))

    print(max_score + second_max_score - total_sadness)
