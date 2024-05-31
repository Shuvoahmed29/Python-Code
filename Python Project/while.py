tt = int(input())
for _ in range(tt):
    n, m = map(int, input().split())
    if n>=m:
        diff = n-m
        if diff%2==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")