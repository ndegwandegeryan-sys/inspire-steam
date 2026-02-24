#Name : ndegwandegeryan
#Date : 19/02/2026
# program to illustrate functions in python


def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2
    print(f"the pan is {pan}, and the fire is {moto},add{oil} amount of oil and cook {eggs} eggs")

print("Here is statement 1")

print("Here is statement 2")

cook_egg()

print("Here is statement 3")

#Bus fare creating function

def create_fare(route,distance,is_rush_hour):

    fare = distance * 10
    if is_rush_hour ==True:
        fare = fare *1.5
    print(f"The fare on route {route} is {fare}")

    return fare

is_rush_hour = True

returened_fare = create_fare("Juja - allsops",7,is_rush_hour)

print(f"The returned fare is : {returened_fare}")
#passing a list as a parameter
def write_all_interests(interests):
    for interests in interests:
        print(f"I am interested in {interests}")
    
all_interests = {"Bike_riding","Hiking" , "painting", "poetry"}

write_all_interests(all_interests)