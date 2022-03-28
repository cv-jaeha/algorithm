cnt = int(input())
list = list(map(int, input().split()))

num1 = 1000000
num2 = -1000000

for i in list:
    num = i
    if num < num1:
        num1 = num
    if num > num2:
        num2 = num

print(num1, num2)