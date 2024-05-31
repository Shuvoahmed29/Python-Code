n = int(input("Enter number: "))
for x in range(1,n+1,1):
    for y in range(0,x,1):
        print("*",end='')
    print("")
print("---------------------------")
for x in range(1,n+1,1):
    print((2*x-1)*"*")