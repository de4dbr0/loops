m=input("input m: ")
n=input("input n: ")
n=int(n)
m=int(m)
sum=0
while m<n:
    m +=1
    if m % 7 == 0:
        sum=sum+m
    
print("sum of all numbers that are dividable by 7 is",sum)   