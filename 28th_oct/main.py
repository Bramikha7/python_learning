# def vowels(words):
#     new=[]
#     for i in words:
#         if i in ["a","e","i","o","u"]:
#             new.append(i)
#     print(new)   
    
# vowels("education")    
    

# def max_vowels(words):
#     new={}
#     vow=["a","e","i","o","u"]
#     for i in words:
#         count=0
#         for j in i:
#             if j in vow:
#                 count=count+1
#         new.update({count:i})
#     print(max(new.items()))

# max_vowels(["cat", "eagle", "umbrella", "sky"]) 

# def even_odd(n):
#     a=0
#     b=0
#     for i in n:
#         if i%2==0:
#             a=a+1 
#         elif i%2!=0:
#             b=b+1
#         else:
#             print("Invalid Input")
#     print("Even= ",a , "Odd= ",b) 


# even_odd([1, 2, 3, 4, 5, 6, 7])               


def two_alternative(list1,list2):
    new=[]
    for i in range(0,len(list1)):
        new.append(list1[i])
        new.append(list2[i])
    print(new)
two_alternative()        