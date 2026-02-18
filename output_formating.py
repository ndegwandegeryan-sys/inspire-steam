#Name : ndegwandegeryan
#Date : 17/02/2026
# program to format the output in 

name = "Ryan Ndegwa"

weight = 56 #weight ni kgs


favourite_team = "arsenal"

height = 150.1 # height in cm

#1.Format using print(f"()")


print(f"my name is {name} and i weigh {weight} kgs.")

#using f string
msg = f"my name is {name} and i support {favourite_team}"
print(msg)  

# using {} and .format()

print("my name is {0} and i am {1}cm tall ".format(name,height))

#using output specifiers as stings
print("The value of pie is approximately %.3f")
print("i support %S " %favourite_team)


