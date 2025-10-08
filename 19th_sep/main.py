
1st sum
a=int(input("Enter the number= "))
b=int(input("Enter the number= "))
c=a+b
if c%2==0:
    print("Even")
else:
    print("odd")    

10th sum
a=input("Enter the payment mode= ")
match a:
    case "UPI":
        print("You selected UPI payment")
    case "Card":
        print("You selected Debit/Credit Card payment")
    case "NetBanking":
        print("You selected Net Banking")
    case "COD":
        print("You selected Cash on Delivery")
    case _:
        print("Invalid Payment Mode")


8th sum
a=int(input("Enter the show time= "))
if a>=9 and a<=12:
    print("Morning Show")
elif a>12 and a<=16:
    print("Matinee Show")
elif a>16 and a<=20:
    print("Evening show")
elif a>20 and a<=24:
    print("Night Show")
else:
    print("Invalid time")

7th sum
path=input("Enter your education path= ")
match path:
    case "Science":
        sub=input("choose the subject(Medical / Engineering)= ")
        match sub:
                case "Medical":
                    print("You choose science -> Medical")
                case "Engineering":
                    print("You choose science -> Engineering")
                case _:
                    print("Invalid sub in science")
    case "Commerce":
        sub=input("choose the subject(CA /B.Com)= ")
        match sub:
                case "CA":
                    print("You choose commerce -> CA")
                case "B.Com":
                    print("You choose commerce -> B.Com")
                case _:
                    print("Invalid sub in commerce")
    case "Arts":
        sub=input("choose the subject(History / Literature)= ")
        match sub:
                case "History":
                    print("You choose Arts -> History")
                case "Literature":
                    print("You choose Arts -> Literature")
                case _:
                    print("Invalid sub in Arts")
    case _:
        print("Invalid education path")                

2nd sum
n=int(input("Enter a two digit number"))
a=n//10 
b=n%10
m=a+b
j=a*b
if(m+j)==n:
    print("great")
else:
    print("no") 

6th sum
n=int(input("Enter the number= "))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n) 

5th sum
a=int(input("Enter the side= "))
b=int(input("Enter the side= "))
c=int(input("Enter the side= "))
if (a+b<=c) or (a+c<=b) or (c+b<=a):
    print("Not a valid triangle")
elif a==b==c:
    print("Equilateral")
elif a==b or b==c or c==a:
    print("Isosceles")
else:
    print("Scalene") 

3rd sum
m=input("Enter the consumer type(residential/commercial):")
n=int(input("Enter the units consumed:"))
if m=="residential":
    if n>=0 and n<=100:
        b=n*3
        print("bill=",b)
    elif n>=101 and n<=200:
        b=n*5
        print("bill=",b)
    elif n>200:
        b=n*7
        print("bill=",b)
    else:
        print("invalid unit")
elif m=="commercial":
    if n>=0 and n<=100:
        b=n*5
        print("bill=",b)
    elif n>=101 and n<=200:
        b=n*7
        print("bill=",b)
    elif n>200:
        b=n*10
        print("bill=",b)
    else:
        print("invalid unit")
else:
    print("invalid input") 

4th sum
d=int(input("Enter the distance:"))
if d>=0 and d<=5:
    f=d*10
    if f<=50:
        print("charge is 50")
elif d>=6 and d<=15:
    f=d*8
    if f<=50:
        print("charge is 50")
    else:
        print("charge is ",f)
elif d>15:
    f=d*6
    if f<=50:
        print("charge is 50")
    else:
        print("charge is ",f)
else:
    print("invalid input")

9th sum
value=int(input("Enter the value in kilometers:"))
print("conversion choice: \n 1->convert to meters \n 2->convert to centimeters \n 3->convert to millimeter \n 4->convert to miles")
km=int(input("enter your choice(1-4):"))
match km:
    case 1:
        print(value*1000)
    case 2:
        print(value*100000)
    case 3:
        print(value*1000000)
    case 4:
        print(value*0.621371)
    case _:
        print("invalid conversion")