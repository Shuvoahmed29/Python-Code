n = int(input("Enter number: "))
cunt=0
for x in range(1,n+1,1):
    if n%x==0:
        cunt+=1;
if cunt==2:
    print(f"This {n} is a Prime Number!")
else:
    print(f"This {n} is NOT a Prime Number!")