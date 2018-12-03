#!/usr/bin/python

#Title: Assignment1---Question6
#Author:Merin
#Version:1
#DateTime:01/12/2018 4:00pm
#Summary:Write a program to read string and print each character separately.
#        a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
#        b) Repeat the string 100 times using repeat operator *
#        c) Read string 2 and concatenate with other string using + operator.


string=input('Enter a string(within quotes):')
print "Each character of the string:",
for x in range(len(string)):
    print string[x],

#a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
print "\nSubstrings are :",string[0:4:1],'\n',string[4:len(string):1]

#b) Repeat the string 100 times using repeat operator *
print "Repeat string 100 times:",string*100

#c) Read string 2 and concatenate with other string using + operator.
string2=input('Enter another string(within quotes):')
print "Concatenated string:",string+string2
     

