#Name : ndegwandegeryan
#Date : 17/02/2026
# program to perform arithmetic operations

f_number = 12 #first number
s_number = 34 #second number

sum_number =f_number + s_number
diff_number= f_number - s_number
product_number = f_number * s_number
quotient_number = f_number / s_number

print ("the sum of the numbers %d" %sum_number)
print ("the quotient of the numbers %f" %quotient_number)
print ("the difference of the numbers %d" %diff_number)
print ("the product of the numbers %d" %product_number)

#modulus - remainder
print(7%2)


#Even and odd numbers

for x in range (0,21):
    if(x%2 ==1):
        print(f"{x} is an odd number")
    elif(x%2 ==0):
        print(f"{x} is an even number")