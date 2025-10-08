#Assignment operator

x=5
y=2
print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)

#to find a number whether it is even or odd

n=int(input("Enter a number: "))
print(n)
if n%2 == 0:
    print("even")
else:
    print("odd")    

#to find a year whether it is leap year or not

A =int(input("Enter the A: "))
if A%4==0:
    print("Y")
else:
    print("N")  

# to find a number whether it is divisible by 3 or 5

n=int(input("Enter the number: "))
print(n)
if (n%3==0 or n%5==0):
    print("divisible")
else:
    print("not divisible")    

#to find a year whether it is 21st century

y=int(input("Enter the year: "))
if (y>=2001 and y<=2100):
    print("21st century")
else:
    print("Not a 21st century")

#to find a number whether it is divisible by 7

N=int(input("Enter the number: "))
print(N)
if (N%7==0):
    print("Yes")
else:
    print("No") 

#free delivery or charged
n=int(input("Enter the number: "))

if n==500:
    print("Free delivery", n)
    
else:
    print("charged", n+50) 
    
    
#to find a number whether it is divisible by 5
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

t = a+b

if t%5 == 0:
    print("1")
else:
    print("0")    

   


