n=input("input a number: ")
m=0
sum=0
while m<int(n):
    m +=1
    if m%2 == 0:
        continue
    sum=sum+m

print("sum of all odd numbers is",sum)   
