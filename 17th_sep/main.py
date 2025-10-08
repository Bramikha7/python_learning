a=int(input("Enter the number: "))
match a:
    case 12|1|2:
        print("Winter")
    case 3|4|5:
        print("Summer")
    case 6|7|8|9:
        print("Monsoon")
    case 10|11:
        print("Autumn")
    case _:
        print("Invalid")  

# to find whether the given alphabet is vowel not

n=input("Enter the character= ")
match n:
     case "a"|"e"|"i"|"o"|"u":
         print("Vowel") 
     case _:
         print("Consonant")
