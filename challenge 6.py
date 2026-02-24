#Name : ndegwandegeryan
#Date : 17/02/2026
# program to illustrate diamond in python

n = 5

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
