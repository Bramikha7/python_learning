Question 1:
A cinema charges:
* ₹150 for ages under 18
* ₹250 for ages 18–60
* ₹100 for ages above 60
Write a program that asks for age and prints the ticket price.
Sample Input:
65
Sample Output:
100

n=int(input("Enter the age: "))
if n <=18:
    print (150)
elif n>18 and n<=60:
    print(250)
elif n>=60:
    print(100)
else:
    print("Invalid Input")            

Question 2:
A stadium sells entry passes with the following rules:
* If age < 12 → Ticket = ₹50
* If age between 12–59 → Ticket = ₹120
* If age ≥ 60 → Ticket = ₹80
Additionally, if the person’s age is a Even number, give a ₹5 discount.
Get the input from the user and return the final discounted stadium ticket price.
Sample Input:
59
Sample Output:
120

n=int(input("Enter the age= "))
if n<=12:
    price=50
elif n>12 and n<=59:
    price=120
else:
    price=80
if n%2==0:
    total=price-5
    print(total)    
              

Question 3:
A shopkeeper has n mangoes.
He wants to pack them into baskets, with 5 mangoes in each basket.
Write a program to calculate:
* How many full baskets can be made
* How many mangoes will be left
Sample Input:
23
Sample Output:
Full Basket is 4
Left Over mangoes is 3

n=int(input("Enter the number of mangoes= "))
full=n//5
over=n%5
print("Full Basket is ",full)
print("Left over mangoes is ",over)


Question 4:
A child has n candies and eats one candy each day until all are finished.
Write Python program to print how many candies the child ate and how many are left each day.
Sample Input:
3
Sample Output:
Day 1 = 2 left
Day 2 = 1 left
Day 3 = 0 left

n=int(input("Enter the number of candies= "))
for i in range(1,n+1):
    left=n-i
    print("Day", i, "=", "left", left)


Question 5:
An employee gets a monthly salary.
* If sales ≥ 100 units → bonus = 10%
* 50–99 units → bonus = 5%
* <50 → no bonus
Write a program that asks for salary and sales and prints total salary including bonus.
Sample Input:
Enter your salary 40000
Enter your sales 120
Sample Output:
Bonus = 4000
Total Salary = 44000

s=int(input("Enter your salary:"))
sales=int(input("Enter your sales:"))
if s>0:
    if sales>0 and sales<50:
        print("No bonus")
        print("Total sales:",s)
    elif sales<=99 and sales>=50:
        b=s*5/100
        print("Bonus:",b)
        print("Total sales:",s+b)
    elif sales>=100:
        b=s*10/100
        print("Bonus:",b)
        print("Total sales:",s+b)
    else:
        print ("invalid input")
else:
    print("Invalid input")        

Question 6:
Earnings of a Salesperson:
* 5% commission for sales ≤ ₹5000
* 10% for sales 5001–10000
* 15% for sales > 10000
Input weekly sales of the salesperson and calculate commission.
Test Cases with their output:
7000 -> 700
12000 -> 1800
11000 -> 1650

n=int(input("Enter the weekly sales of the salesperson:"))
if n>0 and n<=5000:
    print(n,"->",n*5/100)
elif n>=5001 and n<=10000:
    print(n,"->",n*10/100)
elif n>10000:
    print(n,"->",n*15/100)
else:
    print("Invalid input")


Question 7:
Multi-Item Shopping Discount
* Price > 100 → 10% discount
* Price 50–100 → 5% discount
* Price <50 → no discount
Print discounted price per item
Test cases with their output:
200 → 180
80 → 76
40 → 40
150 → 135

p=int(input("enter the price:"))
if p>0 and p<50:
    print("no discount")
elif p>=50 and p<=100:
    d=p*5/100
    print("The discounted price is",d)
elif p>100:
    d=p*10/100
    print("the discounted price is",d)
else:
    print("Invalid input")

Question 8:
A file manager needs to classify files based on their extension.
.csv  → print output as "This is an Excel File"
.jpg  → print output as "This is a JPEG File"
.doc  → print output as "This is a Word File"
.pdf → print output as "This is a PDF File"
.py → print output as "This is a Python File"
.Any other input, print output as "Unknown File Type"
Print the result based on the input
Sample Input:
.csv
Sample Output:
This is an Excel file
Sample input:
.py
Sample Output:
This is a Python File

f=input("Enter the file extension:")
match f:
    case ".csv":
        print("This is an Excel file")
    case ".jpg":
        print("This is a JPEG file")
    case ".doc":
        print("This is a word file")
    case ".pdf":
        print("This is a PDF file")
    case ".py":
        print("This is a python file")
    case _:
        print("Unknown File Type")

Question 9:
Taxi charges:
* First 10 km → ₹15/km
* Next 20 km → ₹12/km
* Beyond 30 km → ₹10/km
Estimate the Taxi charges based on the input and print the output.
Sample Input:
15  → 180
35 → 350
10 → 150

km=int(input("Enter the distance:"))
if km>0 and km<=10:
    f=km*15
    print(f)
elif km>10 and km<=20:
    f=(10*15)+(km-10)*12
    print(f)
elif km>20 and km<=30:
    f=(10*15)+(20*12)+(km-30)*10
    print(f)
else:
    print("Invalid input")

Question 10:
Lily is N years old.
On every odd birthday (1, 3, 5, …) → she gets 1 toy.
On every even birthday (2, 4, 6, …) → she gets money.
The money starts at ₹10 on her 2nd birthday.
On each next even birthday, it increases by ₹10 more:
2nd birthday → ₹10
4th birthday → ₹20
6th birthday → ₹30
and so on.
At the end, print the following:
* Number of toys Lily has.
* Total money she has (money from even birthdays after brother takes ₹1).
Input
* Lily’s age (N)
* Nothing else (price of toys is not needed because we are not selling)
Output
* Number of toys
* Total money (formatted with 2 decimal places)
Sample TestCase:
Input
10
Output
5
150.00
Explanation:
Toys → 1,3,5,7,9 → 5 toys.
Money → 10 + 20 + 30 + 40 + 50 = ₹150.

age=int(input("Enter the age:"))
start=1
toy=0
money=0
while start<=age:
    if start%2==0:
        money=money+10
    else:
        toy=toy+1
    start=start+1
print(toy)
print(money)