#to find  a number whether it has a discount or not

n=int(input("Enter the Amount= "))
if n>=1000:
    C=n-n*10/100
    print("The final amount: ",C)
elif n<1000 and n>=500:
    C=n-n*5/100
    print("The final amount: ",C)
elif n< 500:
    print("The final amount: ",n)    
    print("No Discount")

#to find a largest number

x=int(input("Enter the number= "))
y=int(input("Enter the number= "))
z=int(input("Enter the number= "))
if x>y and x>z:
    print("x is greater")
elif y>z:
    print("y is greater") 
else:
    print("z is greater")       