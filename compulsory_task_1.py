'''==== Capstone project template ====
This template provides the skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add code for compulsory task 2 and complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
import time

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
database = {}

user_name = input("Enter your user name:")
print(user_name)
password = input("Enter a password:")  

with open("user.txt") as file:
    content = file.readlines()

    
    sort_out = [cont.strip("\n") for cont in content]
    seperate = [sort_out[i].split("i") for i in range(len(sort_out))]

for i in range(len(seperate)):
    print(seperate)
    database.update({seperate[i][0]: seperate[i][1].strip()})
    
if user_name:
    print('Login succesful:'+ user_name + '\n')

for key, value in database.items():
    if key == user_name and value == password:
        print("Login Successfully")

        break

while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        user_name = input("Enter user name:")
        password = ("Enter password:")
        confirm_password = ("Confirm Password:") 

        if password == confirm_password:
          with open("user.txt","a") as file:
            file.write("\n {user_name},{password}")
        else:
          print("Password entered is incorrect")
    

    elif menu == 'a': 
        assign_user =input("Enter a assign task of choice:")

        title_task = input("Enter task title:")

        task_desciption = input("Enter task decription:")

        due_date = input("Enter the due date:")

    
    

    
    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
# Do a code
    elif menu == 'vm':
        
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        
        with open('tasks.txt', 'r') as file:                               
            print('My Tasks')           
            for line in file:                                                
                if line.split(',')[0].strip() == user_name:  

    
    elif menu == 'e':    
        print('Goodbye!!!')   
        exit()


    else:
        print("You have made a wrong choice, Please Try again")