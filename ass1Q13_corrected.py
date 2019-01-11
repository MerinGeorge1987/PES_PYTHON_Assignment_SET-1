#!/usr/bin/python

#Title: Assignment1---Question12
#Author:Merin
#Version:1
#DateTime:02/12/2018 4:00pm
#Summary:Write a program to find the biggest of 4 numbers.
#        a) Read 4 numbers from user using Input statement.
#        b) extend the above program to find the biggest of 5 numbers.
#       (PS: Use IF and IF & Else, If and ELIf, and Nested IF)




#Read 4 numbers from user
a,b,c,d=map(int,input("Enter 4 numbers(separated by commas):").split(','))

#Biggest of 4 numbers
if a>b:
    if a>c:
        if a>d:
            print (a,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=a
        elif d>a:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif a==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c>a:
        if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
        elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif c==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c==a:
        if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
        elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif c==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
elif b>a:
    if b>c:
        if b>d:
            print (b,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=b
        elif d>b:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif b==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c>b:
         if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
         elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
         elif d==c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c==b:
        if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
        elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif c==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d         
elif b==a:
    if b>c:
        if b>d:
            print (b,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=b
        elif d>b:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif b==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c>b:
        if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
        elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif c==d:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
    elif c==b:
        if c>d:
            print (c,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=c
        elif d>c:
            print (d,"is the biggest of %d,%d,%d and %d"%(a,b,c,d))
            big=d
        elif c==d:
            print ("All are same")
            big=d    

#Biggest of 5 numbers
e=int(input("Enter a number:"))
if big>e:
    print (big,"is the biggest of %d,%d ,%d,%d and %d"%(a,b,c,d,e))
elif e>big:
    print (e,"is the biggest of  %d,%d ,%d,%d and %d"%(a,b,c,d,e))
else:
    print ("All are same")
    
    


