lst = []
for i in range(10):
    lst.append(int(input()))

arr = []
for j in range(10):
    arr.append(lst[j] % 42)

cnt = []
count = 0
for k in range(10):
    if arr[k] in cnt:
        continue
    else:
        cnt.append(arr[k])
        count += 1

print(count)