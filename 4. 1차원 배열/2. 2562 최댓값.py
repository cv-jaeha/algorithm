list = []
for i in range(9):
    n = int(input())
    list.append(n)

num = 0
count = 0
for i in range(9):
    if num < list[i]:
        num = list[i]
        count = i+1
    else:
        continue

print(num)
print(count)