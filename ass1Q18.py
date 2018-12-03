#!/usr/bin/python

#Title: Assignment1---Question18
#Author:Merin
#Version:1
#DateTime:02/12/2018 10:30pm
#Summary:Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
#        a) By using For loop 
#        b) By using while loop
#        c) Let mystring ="Hello world"
#        print each character of mystring in to separate line using appropriate loop structure.

#a) By using For loop
print "FOR Loop:"
y=100
for x in range(100):
    print x+1,'\t',y
    y=y-1
         
#b) By using while loop
print "WHILE Loop:"
x=1;y=100
while x<=100:
    print x,'\t',y
    y=y-1
    x=x+1

#c)Let mystring ="Hello world". print each character of mystring in to separate line using appropriate loop structure.
mystring ="Hello world"
for x in range(len(mystring)):
    print mystring[x]
    
   
