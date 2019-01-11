#!/usr/bin/python

#Title: Assignment1---Question2
#Author:Merin
#Version:1
#DateTime:01/12/2018 3:40pm
#Summary:Write a program to find the biggest of 3 numbers (Use If Condition)

print ("******Assignment1 Question2******")
print ("****Find the biggest of 3 numbers****")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
    
if a>b:
    if a>c:
        print (a,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c>a:
        print (c,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c==a:
        print (c,"is the biggest of %d,%d and %d"%(a,b,c))
elif b>a:
    if b>c:
        print (b,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c>b:
        print (c,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c==b:
         print (c,"is the biggest of %d,%d and %d"%(a,b,c))      
elif b==a:
    if b>c:
         print (b,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c>b:
        print (c,"is the biggest of %d,%d and %d"%(a,b,c))
    elif c==b:
       print ("All are same") 
        
        
        
        



