#!/usr/bin/python

#Title: Assignment1---Question5
#Author:Merin
#Version:1
#DateTime:03/12/2018 12:00pm
#Summary:Write a program to receive 5 command line arguments and print each argument separately.
#        Example: >> python test.py arg1 arg2 arg3 arg4 arg5
#        a) From the above statement your program should receive arguments and print them each of them. 
#        b) Find the biggest of three numbers, where three numbers are passed as command line arguments.



import sys

#a) From the above statement your program should receive arguments and print them each of them.
print 'Arguments are', 
x=1
while x<=len(sys.argv):
    print sys.argv[x],',',
    x=x+1

#b) Find the biggest of three numbers, where three numbers are passed as command line arguments.
#Assumption: First 3 arguments are the three numbers

a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
if a>b and a>c:
    print a," is the biggest of %d,%d,%d",%(a,b,c)
elif b>a and b>c:
    print b," is the biggest of %d,%d,%d",%(a,b,c)
elif c>a and c>b:
    print c," is the biggest of %d,%d,%d",%(a,b,c)
else:
    print "All are same"
    


    



