#!/usr/bin/python

#Title: Assignment1---Question16
#Author:Merin
#Version:1
#DateTime:02/12/2018 5:30pm
#Summary:Write program to perform following:
#        i) Check whether given number is prime or not.
#        ii) Generate all the prime numbers between 1 to N where N is given number.


#i) Check whether given number is prime or not.
num1=input ("Enter a number:")

x=2;flag=0
while x<=num1/2:
    if num1%x==0:
        flag=flag+1
    x=x+1

if flag==0:
    print num1," is a prime number"
else:
    print num1," is not a prime number"

#ii) Generate all the prime numbers between 1 to N where N is given number.
N=input ("Enter a number: ")
print "Prime numbers between 1 to %d :"%N,

for y in range(2,N,1):
    x=2;flag=0
    while x<=y/2:
        if y%x==0:
            flag=flag+1
            break
        x=x+1
    if flag==0:
        print y,",",
    

    
   
