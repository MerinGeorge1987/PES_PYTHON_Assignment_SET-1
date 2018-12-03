#!/usr/bin/python

#Title: Assignment1---Question12
#Author:Merin
#Version:1
#DateTime:02/12/2018 3:20pm
#Summary:Read 10 numbers from user and find the average of all.
#        a) Use comparison operator to check how many numbers are less than average and print them
#        b) Check how many numbers are more than average.
#        c) How many are equal to average.




#Read 10 numbers from user
num=[]
print "enter 10 numbers:"
for x in range(10):
    num.append(input())
print num

#average of all.
avg=0
for x in range(10):
    avg=avg+num[x]
avg=avg/10
print "Average=",avg

#a) numbers less than average and print them
print "Numbers less than average:",
for x in range(10):
    if num[x]<avg:
        print num[x],",",

#b) numbers are more than average.
print "\nNumbers more than average:",
for x in range(10):
    if num[x]>avg:
        print num[x],",",

#c) equal to average
print "\nNumbers equal to average:",
for x in range(10):
    if num[x]==avg:
        print num[x],",",






