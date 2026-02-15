#Name : ndegwandegeryan
#Date : 13/02/2026
#program to calculate arithmetic progresson

#calculating the nth term

a = int(input("enter the first_number:"))
n = int(input("enter the number of terms:"))
d = int(input("enter the common difference :"))

nth_term = a + (n - 1) *d

sn = (n/2) * ( 2*a + (n-1) *d )
print(f"the nth term is : {nth_term}")
print(f"the sum of the terms is : {sn}")
