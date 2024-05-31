i = 1
while i<20:
    if i%2==0:
        print(i)
    i+=1

#Sum of n numbers
n = int(input("Enter the last number: "))
i = 0
sum=0
while i<=n:
    sum+=i
    i+=1
print(f"Summation is : {sum}")