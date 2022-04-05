a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))

for j in range(10):
    print(result.count(str(j)))

# Reference : https://pacific-ocean.tistory.com/34