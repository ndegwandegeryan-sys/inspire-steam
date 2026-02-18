#Name : ndegwandegeryan
#Date : 13/02/2026
#program to calculate geometric progresson

a = int(input("enter the first_number:"))
n = int(input("enter the number of terms:"))
r = int(input("enter the common ratio:"))

nth_term = a* r** n-1
sum_of_terms = (a*(r**n - 1)) / (r-1)

print(f"the nth term is : {nth_term}")
print(f"the sum of the terms is :{sum_of_terms}")