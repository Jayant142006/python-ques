"""
Q12 Write a program to find the sum of digits of a number.
"""

num = int(input("enter a no. = "))
sums = 0
while(num>0):
    temp = num%10
    sums += temp
    num = num//10
print(sums)
