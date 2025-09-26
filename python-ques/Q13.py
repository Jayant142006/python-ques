"""
Q13 Write a program to find the factorial of a number.
"""

a=int(input("Enter a No: "))
factorial=1
for i in range(1,a+1):
    factorial *=i
print("factorial is:",factorial )
