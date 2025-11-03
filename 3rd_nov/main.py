def sentence(words):
    new=""
    for i in words:
        if i ==" ":
            new=new+"-"
        else:
            new=new+i
    print(new)        
        
        
sentence('python learning')  
      
        
        
def element(num,check):
    for i in range(0,len(num)):
        if num[i]==check:
            print(i)
            
element([11,22,33,44,55],33) 




def score(a,b):
    count=0
    for i in range(0,len(a)):
        if a[i]<b[i]:
            count=count+1
    print(count)
    
score([55,65,98,90,89],[65,75,90,91,88])

