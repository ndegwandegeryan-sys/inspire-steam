#Name : ndegwandegeryan
#Date : 19/02/2026
# program to illustrate classes in python


class human:
    #first we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain =True
    warm_blooded =True
    city = "Nairobi"

    # we then create a constructor for the class/object
    # The constructor will be used to create 
    def __init__(self , name , age):
        self.human_name = name
        self.human_age = age


    def tell_story(self):
        print(f"Hello , I am {self.human_name} and here is a story")
        print("Today i slept at four in the morning and woke up at six approximately 2 hours after i slept meaning i am currently sleepy")


#create the humans
amani = human("Amani","18")
Ryan = human("Ryan","18")

#use the humans
amani.tell_story()
print("Amani's age is :",amani.human_age)

#Modify one fo the objects without modifying other objects

Ryan.city = "Kiambu"

print(f"Ryan's location is {Ryan.city}")
print(f"Amani's location is {amani.city}")