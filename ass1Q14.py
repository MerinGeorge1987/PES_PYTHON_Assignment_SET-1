#!/usr/bin/python

#Title: Assignment1---Question14
#Author:Merin
#Version:1
#DateTime:02/12/2018 4:40pm
#Summary:Write a program to create two list A &B such that List A contains Employee Id, List B contain Employee name(minimum 10 entries in each list) &perform following operation
#        a) Print all names on to screen
#        b) Read the index from the  user and print the corresponding name from both list.
#        c) Print the names from 4th position to 9th position
#        d) Print all names from 3rd position till end of the list
#        e) Repeat list elements by specified number of times (N- times, where N is entered by user)
#        f)  Concatenate two lists and print the output.
#        g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

A=['01','02','03','04','05','06','07','08','09','10']
B=['Joe','Anna','Kiran','Anita','Sultana','Rahul','Priya','Anil','Madhu','Eva']

#a) Print all names on to screen
print "Names",B

#b) Read the index from the  user and print the corresponding name from both list.
i=input('Enter an index(number between 0 & 9):')
print " Corresponding employee id & name is %s & %s"%(A[i],B[i])

#c) Print the names from 4th position to 9th position
print "Names from 4th to 9th position:",B[3:9:1]

#d) Print all names from 3rd position till end of the list
print "Names from 3rd position till end of the list:",B[2::1]

#e) Repeat list elements by specified number of times
n=input ("enter number of times list need to be printed:")
print "Repeating employee id list %d times"%n,A*n
print "Repeating employee name list %d times"%n,B*n

#f)  Concatenate two lists and print the output.
c=A+B
print "Concatenated list",c

#g) Print element of list A and B side by side.
for x in range(10):
    print A[x],'\t',B[x]



