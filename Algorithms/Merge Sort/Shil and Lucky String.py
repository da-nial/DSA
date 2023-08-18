# n = int(input())

# s = list(input())

s = "nsclgrcdxjnpxtxzsudiqmncpybrkifxbhihylmxubmtultpiwxykmczkgtvoauphdyiqmfmnufifyzpwynilqixydumdpcmucwkpcwcybmfclvamijxatwawrnbirpctmmiqknolbtppoqbzzybsucqnptviixbulmkvbajcuyrkosjnsnhppxcgsaobzrvlfiigirjescpgvywplfecfjixjyyiswvxgggozrtrtiaqiygwdmyivjigjgr"
s = list(s)
n = len(s)

first_half = s[:n // 2]
second_half = s[n // 2:]

first_half.sort()
second_half.sort()

num_greater = 0
num_equal = 0
num_less = 0

for i in range(n // 2):
    if first_half[i] > second_half[i]:
        num_greater += 1
    elif first_half[i] == second_half[i]:
        num_equal += 1
    else:
        num_less += 1

print(f"n//2: {n//2}")
print(f"num_greater: {num_greater}")
print(f"num_equal: {num_equal}")
print(f"num_less: {num_less}")

# print(n // 2 - max([num_greater, num_equal, num_less]))
