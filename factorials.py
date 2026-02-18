#Name : ndegwandegeryan
#Date : 16/02/2026
#program to calculate the factorial of numbers

number = int(input("enter the number x:"))

factorial = 1

for x in range (1,number + 1 ) :
    factorial*= x
print(f"{number}! = {factorial}")
