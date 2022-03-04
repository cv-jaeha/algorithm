I = int(input())
for i in range(1, I+1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")