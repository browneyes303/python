
#! EASY

#? 1. Hello You!

# name_of_user = input("What is your name? ")

# print("Hello {}, it is very nice to meet you!".format(name_of_user))

#? 2. HELLO YOU

# name_of_user = input("WHAT IS YOUR NAME? ")
# x = name_of_user.upper()
# print("HELLO {}, IT IS VERY NICE TO MEET YOU!".format(x))

#? 3. Madlib

# print("""
# Please fill in the blanks below:
# ___(name's)___ favorite subject in school is ___(subject)___.
# """)

# name = input("What is a name? ")
# subject = input("What is a subject? ")

# print(f"{name}'s favorite subject in school is {subject}")

#? 4. Day of the Week

# day = 7
# day = int(input('Enter the name of a Day (0-6): '))

# if day != 7:
#     if day == 0:
#         result = "Sunday"
#     elif day == 1:
#         result = "Monday"
#     elif day == 2:
#         result = "Tuesday"
#     elif day == 3:
#         result = "Wednesday"
#     elif day == 4: 
#         result = "Thursday"
#     elif day == 5:
#         result = "Friday"
#     elif day == 6:
#         result = "Saturday"
#     else:
#         result = "This is not an option"

# print(result)

#? 5. Work of Sleep In

# day = 7
# day = int(input('Enter the name of a Day (0-6): '))

# if (day < 1) or (day > 5):
#     result = "Sleep In"
# else:
#     result = "Go to Work"

# print(result)

#? 6. Celsius to Fahrenheit

# c = int(input("Enter a temperature in Celsius: "))

# f = (c * 9/5) + 32

# print(f)

#? 7. Looping from 1 to 10

# count = 0

# while(count < 10):
#     count+=1
#     print(count)

#? 8. n to m

# start = int(input('Start From >> '))
# stop = int(input('End On >>'))

# for i in range(start,(stop+1)):
#     print(i)
#     start+=1
    
#? 9. Print a square

# height = 5

# for i in range(height,0,-1):
#     print('*' * 5)

#? 10. Print a Square II

# height = int(input("How big is the square?  "))

# for i in range(height,0,-1):
#     print('*' * height)

#! MEDIUM

#? 1. Tip Calculator

# good = .20
# # fair = .15
# # bad = .10

# # bill = int(input("Total bill amount?  " ))
# # service = input("Level of service?  ")

# # if service == "good":
# #     result = bill * good
# # elif service == "fair":
# #     result = bill * fair
# # elif service == "bad":
# #     result = bill * bad


# # bill_total = bill + result

# # print("Tip amount: {}".format(result))
# # print("Total amount: {}".format(bill_total))

#? 2. Tip Calculator 2

# good = .20
# fair = .15
# bad = .10

# bill = int(input("Total bill amount?  " ))
# service = input("Level of service?  ")
# split = int(input("Split how many ways?  " ))

# if service == "good":
#     result = bill * good
# elif service == "fair":
#     result = bill * fair
# elif service == "bad":
#     result = bill * bad


# bill_total = bill + result
# bill_split = bill_total / split

# print("Tip amount: {}".format(result))
# print("Total amount: {}".format(bill_total))
# print("Amount per person: {}".format(bill_split))


#? 3. How many coins

# coins = 0
# answer = 'yes'

# while(answer != 'no'):
#     print(f'You have {coins} coins.')
#     answer = input('Do you want another?  ')

#     if answer != 'no':
#         coins += 1
#     else:
#         print('Bye')


#? 4. Print a Box

width = int(input("Width?  " ))
height = int(input("Height?  " ))

for i in range(height,0,-1):
    print('*' * height)

#? 5. Print a Triangle

# height = 4

# for i in range(height,0,-1):
#     print(i* ' ' + (height-i) * '*' + '*' * (height+1-i) + i* '')

#? 6. Multiplication Table



