#!/usr/bin/python

#Title: Assignment1---Question15
#Author:Merin
#Version:1
#DateTime:02/12/2018 5:10pm
#Summary:Create a list of 5 names and check given name exist in the List.
#        a) Use membership operator (IN) to check the presence of an element.
#        b) Perform above task without using membership operator.
#        c) Print the elements of the list in reverse direction.



B=['Joe','Anna','Kiran','Anita','Sultana']
print "List:",B

#a) Use membership operator (IN) to check the presence of an element.
n=raw_input("Enter element to be checked:")
if  n in B:
    print "Found"
else:
    print "not found"

#b) Perform above task without using membership operator.
flag=0
for x in range(5):
    if  n==B[x]:
        flag=flag+1

if flag>0:
    print "Found"
else:
    print "not found"
    
#c) Print the elements of the list in reverse direction.
print "List in reverse:",B[::-1]
