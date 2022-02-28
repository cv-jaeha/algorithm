H, M = input().split()

if int(M) >= 45:
    print(f"{int(H)} {int(M)-45}")
elif int(H) > 0:
    print(f"{int(H)-1} {60 - (45 - int(M))}")
else:
    print(f"23 {60 - (45 - int(M))}")