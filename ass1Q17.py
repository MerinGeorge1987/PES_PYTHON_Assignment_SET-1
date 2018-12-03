#!/usr/bin/python

#Title: Assignment1---Question17
#Author:Merin
#Version:1
#DateTime:02/12/2018 8:30pm
#Summary:Write program to find thebiggest and Smallest of N numbers.
#        PS: Use the functions to find biggest and smallest numbers. 


#Function to find biggest
def Biggest(list1,N):
    list1.sort()
    return (list1[N-1])

#Function to find smallest
def Smallest(list1):
     list1.sort()
     return (list1[0])

LIST=map(int,raw_input("Enter numbers separated by commas:").split(','))
N=len(LIST)

#Function Call
print "Smallest number:",Smallest(LIST)
print "Biggest number:",Biggest(LIST,N)
         
    

    
   
