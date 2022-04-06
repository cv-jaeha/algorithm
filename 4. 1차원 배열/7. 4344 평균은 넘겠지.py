n = int(input())

for i in range(n):
    lst = []
    lst = list(map(int, input().split()))

    total = 0
    for j in range(1, len(lst)):
        total += lst[j]
    result = total / lst[0]

    count = 0
    for k in lst:
        if k > result:
            count += 1

    print(f"{round((count / (len(lst)-1)) * 100, 3)}%")