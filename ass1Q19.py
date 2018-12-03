#!/usr/bin/python

#Title: Assignment1---Question19
#Author:Merin
#Version:1
#DateTime:02/12/2018 10:40pm
#Summary:Using loop structures print even numbers between 1 to 100.  
#        a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#           i) Break the loop if the value is 50
#           ii) Use continue for the values 10,20,30,40,50
#        b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#           i) Break the loop if the value is 90
#           ii) Use continue for the values 60,70,80,90


#a) By using For loop print even numbers between 1 to 100
print "using FOR Loop even numbers between 1 to 100:"
for x in range(1,100):
    if x%2!=0:
        pass
    else:
        print x,',',

#i) Break the loop if the value is 50
print "\nBreak the loop if the value is 50:"
for x in range(1,100):
    if x==50:
        break
    elif x%2!=0:
        pass
    else:
        print x,',',

#ii) Use continue for the values 10,20,30,40,50
print "\nUse continue for the values 10,20,30,40,50:"
for x in range(1,100):
    if x==10 or x==20 or x==30 or x==40 or x==50:
        continue
    if x%2!=0:
        pass
    else:
        print x,',',

#b) By using While loop print even numbers between 1 to 100
print "\nusing WHILE Loop even numbers between 1 to 100:"
x=1
while x<100:
    if x%2!=0:
        pass
    else:
        print x,',',
    x=x+1

#i) Break the loop if the value is 90
print "\nBreak the loop if the value is 90:"
x=1
while x<100:
    if x==90:
        break
    elif x%2!=0:
        pass
    else:
        print x,',',
    x=x+1

#ii) Use continue for the values 60,70,80,90
print "\nUse continue for the values 60,70,80,90:"
x=1
while x<100:
    if x==60 or x==70 or x==80 or x==90:
        x=x+1
        continue
    if x%2!=0:
        pass
    else:
        print x,',',
    x=x+1


         
