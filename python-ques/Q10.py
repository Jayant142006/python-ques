"""
Q10 Write a program to print the largest among 3 numbers.
"""

a = int(input("enter first no. = "))
b = int(input("enter second no. = "))
c = int(input("enter third no. = "))
if(a>b and a>c):
    print("first number is the largest")
elif(b>a and b>c):
    print("second number is the largest")
else:
    print("third number is the largest")
