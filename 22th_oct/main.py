1st
def split_the_string(sentence):
    res=sentence.split("-")
    for i in range(0,len(res),+1):
        print(res[i])
split_the_string("Emma-is-a-data-scientist")

1st 
def split_the_string(sentence):
    word=""
    for i in range (0,len(sentence),+1):
        if sentence[i] != "-":
            word=word+sentence[i]
        else:
            print(word)
            word=""
    print(word)
split_the_string("Emma-is-a-data-scientist")

2nd

def word_rev(str1):
    rev_str = str1[::-1]
    print(rev_str)

word_rev("Python")  

3rd

word = "Hello World"
count=0
i=0

while i < len(word):
    n = word[i]
    if word[i] not in "aeiou":
        count=count+1
    i=i+1
print("Number of consonant= ",count) 


4th

def remove_space(word):
    res=word.split()
    result="".join(res)
    print(result)
remove_space("hello world")

5th

def passwords(n):
    special_characters = "!@#$%^&*"
    if len(n) < 8:
        print("Password is not strong")
    else:
        for char in n:
            if char in special_characters:
                print("Password is strong")
                break
        else:
            print("Password is not strong")
passwords("my@password")
passwords("python123")
    

