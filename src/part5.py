
#Asks for the user's name
user=input("enter the user name:")

#Asks for their birth year
birth=int(input("enter the birth year: "))     #-------------> convert to int for input() function 

#Calculates their age (use 2026 as the current year)
age_cal=2026-birth

#Prints a formatted message using an f-string:
print(f'Hello {user}, you are {age_cal} years old. Welcome to your 1% developer journey!')