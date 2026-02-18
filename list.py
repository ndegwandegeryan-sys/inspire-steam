#Name : ndegwandegeryan
#Date : 18/02/2026
# program to show lists in python
 
#list of friends
friends = ["Rachael","Pheobe","Chandler","Monica","Ross",]


print(friends)

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Jack") #adds item on the list
print(friends)

new_friends = ["Faith","Don","Cynthia","Wanjey","Clement"]
print(len(new_friends)) #says the number of things on the list

#new list of students
students = friends + new_friends
print(students)

students.pop() #remove last item
print(students)

students.insert(5,"Jenny")
print(students)

students.insert(9,"James")
print(students)

students.extend("Dan")
print(students)

students.remove("Ross")
print(students)

new_students = students.copy()
print(students)