n = int(input())

ox = []
for _ in range(n):
    ox.append(input())

for i in range(n):
    result = 0
    last_X = -1
    for j in range(len(ox[i])):
        if ox[i][j] == 'O':
            result += j - last_X
        else:
            last_X = j
    print(result)