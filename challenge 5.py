#Name : ndegwandegeryan
#Date : 16/02/2026
# calculate income tax

salary = int(input(" enter the gross salary :"))

if salary < 50000 :
    tax = (2.5 *salary) /100
    net_salary = salary - tax

elif salary >50000 and salary < 100000:
    tax = (0.045*salary)
    net_salary = salary -tax

elif salary >100000 :
    tax = (0.075 *salary)
    net_salary = salary - tax

print(f"Gross salary = {salary}")
print(f"net salary = {net_salary}")
print(f"tax = {tax}")
