n = int(input("Enter last number: "))
for x in range(1,n+1,1):
    for i in range(1,x+1,1):
        print(i,end=' ')
    print()