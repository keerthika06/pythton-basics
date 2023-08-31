def say_hi():
    print("hello user")

say_hi()



def max_no(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

print(max_no(5 , 7 , 3))
    