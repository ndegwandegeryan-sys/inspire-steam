#Name : ndegwandegeryan
#Date : 24/02/2026
#program to perform file operating

#create new file
new_file = open("student_data.txt","r+")

#write to new file
new_file.write("{student name :Ryan Ndegwa , ID : 0346578 , email : ndegwandegeryan@gmail.com} ")

#read from the file
new_file = open("{student name :Ryan Ndegwa , ID : 0346578 , email : ndegwandegeryan@gmail.com}")

data = new_file.read()

new_file.close()

# us os module
import os 
os.remove(remove.txt)

#delete folder
os.rmdir("Folder")