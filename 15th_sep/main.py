# Given the (x,y) coordinates a point check in which quadrants the point lies.

x=int(input("Enter the value of x= "))
y=int(input("Enter the value of y= "))
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2") 
elif x<0 and y<0:
    print("Quadrant 3")
elif x>0 and y<0:
    print("Quadrant 4")
else:
    print("Invalid")               

# Switch Case (Match Case)

month=int(input("Enter the month= "))

match (month):
     case 1:
          print("january")
     case 2:
          print("Feb")
     case 3:
          print("March")
     case 4:
          print("April")
     case 5:
          print("May")
     case 6:
          print("June")
     case 7:
          print("July")
     case 8:
          print("August")
     case 9:
          print("September")
     case 10:
          print("October")
     case 11:
          print("November")
     case 12:
          print("december") 
     case _:
          print("Invalid month")  

# to find whether the given number is positive or not.
a=int(input("Enter the number= "))
if a>0:
     print("The number is positive")
elif a<0:
     print("The number is negative")
else:
     print ("The number is zero")          

# to find the single character whether it is vowel or not.

x=input("Enter the single character= ")
if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
     print("The character is vowel")
else:
     print("The character is Consonant")     

# to find 