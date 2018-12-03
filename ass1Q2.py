#!/usr/bin/python

#Title: Assignment1---Question2
#Author:Merin
#Version:1
#DateTime:01/12/2018 3:40pm
#Summary:Write a program to find the biggest of 3 numbers (Use If Condition)

a=10.5
b=7.2
c=20.18
if a>b and a>c:
    print a,"is the biggest of %.2f,%.2f and %.2f"%(a,b,c)
elif b>c and b>a:
    print b,"is the biggest of %.2f,%.2f and %.2f"%(a,b,c)
elif c>a and c>b:
    print c,"is the biggest of %.2f,%.2f and %.2f"%(a,b,c)
else:
    print "All are same"
    



