#!/usr/bin/python

#Title: Assignment1---Question4
#Author:Merin
#Version:1
#DateTime:01/12/2018 3:55pm
#Summary:Write a program to find the number is Prime or not

num1=input('Enter a number:')

x=2;flag=0
while x<=num1/2:
    if num1%x==0:
        flag=flag+1
    x=x+1

if flag==0:
    print '%d is a prime number'%num1
else:
     print '%d is not a prime number'%num1  
     

