
1st sum

start=0
end=100
while start<=end:
    if start%5==0:
        print(start)
    start=start+1 

2nd sum

n=int(input("Enter the number= "))
start=1
end=10
while start<=end:
    print(start*n)
    start=start+1  

3rd sum

start=1
end=5 
total=0
while start<=end:
    total=total+start
    start=start+1
print(total)    