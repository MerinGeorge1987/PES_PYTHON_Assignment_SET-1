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
a,b,c,d=map(int,raw_input("Enter 4 numbers(separated by commas):").split(','))

#Biggest of 4 numbers
if a>b and a>c and a>d:
    print a,"is the biggest of %.2f,%.2f ,%.2f and %.2f"%(a,b,c,d)
    big=a
elif b>c and b>a and b>d:
    print b,"is the biggest of %.2f,%.2f,%.2f and %.2f"%(a,b,c,d)
    big=b
elif c>a and c>b and c>d:
    print c,"is the biggest of %.2f,%.2f,%.2f and %.2f"%(a,b,c,d)
    big=c
elif d>a and d>b and d>c:
    print d,"is the biggest of %.2f,%.2f,%.2f and %.2f"%(a,b,c,d)
    big=d
else:
    print "All are same"

#Biggest of 5 numbers
e=input("Enter a number:")
if big>e:
    print big,"is the biggest of %.2f,%.2f ,%.2f,%.2f and %.2f"%(a,b,c,d,e)
elif e>big:
    print e,"is the biggest of %.2f,%.2f ,%.2f,%.2f and %.2f"%(a,b,c,d,e)
else:
    print "All are same"
    
    


