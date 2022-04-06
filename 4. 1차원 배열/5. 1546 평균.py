n = int(input())
lst = list(map(int, input().split()))

n_max = 0
max_t = -1
for i in range(n):
    if n_max < lst[i]:
        n_max = lst[i]
        max_t = i

result = 0
for j in range(n):
    if max_t == j:
        result += 100
        continue
    else:
        result += ((lst[j] / n_max) * 100)

print(result / n)