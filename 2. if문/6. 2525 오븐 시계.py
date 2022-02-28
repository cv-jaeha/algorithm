H, M = input().split()
m = int(input())
H = int(H)
M = int(M)

if ((M+m) // 60) + H < 24:
    if M + m < 60:
        print(H, M+m)
    else:
        print(H + ((M+m) // 60), (M+m) % 60)
else:
    if M + m < 60:
        print(0, M+m)
    else:
        print((H + ((M+m) // 60)) - 24, (M+m) % 60)