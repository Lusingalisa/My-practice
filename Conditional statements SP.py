## IF STATEMENTS

# number = int(input("Enter a number\n "))
# if number > 10:
#     print("The number is greater than 10") 

# age = int(input("Enter your age\n"))
# if age >=18:
#     print("You are eligible to vote")

# is_logged_in = True
# if is_logged_in:
#     print("Welcome") 

# day = input("Enter the day of the week\n")
# if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
#     print("It is a weekday") 

# temp = int(input("Enter the temperature: "))
# if temp>30:
#     print("It is a hot day") 

# name = input("Enter your name\n")
# if len(name)>5:
#     print("That is a long name") 

# amount=int(input("Enter the order amount: "))
# if amount > 50:
#     print("You qualify for free shipping.") 


## IF-ELSE STATEMENTS

# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd") 

# correct_password = 12345
# password =int(input("Enter the password\n"))
# if password == correct_password:
#     print("Access granted")
# else:
#     print("Access denied") 

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# else:
#     print("Negative or Zero")

# number = int(input("Enter a number\n"))
# if number % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5") 

# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# if num1>num2:
#     print("The first number is larger")
# else:
#     print("The second number is larger") 

# discount_code = "SAVE10"
# code = input("enter your code\n")
# if code == discount_code:
#     print("Discount applied!")
# else:
#     print("Invalid code.") 

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 % num2 == 0:
#     print("they are divisible")
# else:
#     print("They are not divisible") 

# age = int(input("enter your age: "))
# rating = input("Enter the movie rating: ")
# if age >=13 and rating in ["PG-13", "R", "G"]:
#     print("You can watch this movie")
# else:
#     print("You cannot watch this movie")  

# num_1= int(input("enter a number: "))
# num_2 = int(input("enter a number: "))
# if num_1 == num_2:
#     print("They are equal")
# else:
#     print("They are not equal") 


## COMBINING CONDITIONS

# age = int(input("Enter your age: "))
# name = input("Enter your name: ")
# if age >= 18 and name.lower().startswith("a"):
#     print("Welcome VIP!")
# else:
#     print("Welcome!") 

# num = int(input("Enter a number: "))
# if 1 <= num <= 100 and num%2 == 0:
#     print("Valid number")
# else:
#     print("Invalid number") 

# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") 

# score = int(input("Enter the score:"))
# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score <= 89:
#     print("B")
# elif 70 <= score <= 79:
#     print("C")
# elif 60 <= score <= 69:
#     print("D")
# elif score < 60:
#     print("F")
# else:
#     print("Invalid score") 

# weight = int(input("Enter the weight: "))
# if weight == 1:
#     print("Shipping cost is $5")
# elif 1 < weight < 5:
#     print("Shipping is $10")
# else:
#     print("Shipping is $20") 

# age = int(input("Enter your age: "))
# time = input("Eter the time of day: ")
# if age <  12 and time == 'matinees':
#     print("the cost is $5")
# elif age < 12 and time == 'evening':
#     print("the cost is $8")
# elif age > 12 and time == 'matinees':
#     print("The cost is $10")
# else:
#     print("The cost is $13") 

# points = int(input("Enter the points: "))
# lives = int(input("Enter the lives: "))
# if points > 100 and lives >= 3:
#     print("Level up")
# else:
#     print("Keep trying") 

# budget = int(input("enter your budget: "))
# destination = input("Enter your destination: ")
# if budget > 1000 and destination == "Europe":
#     print("Let's book a trip to Europe!")
# else:
#     print("Consider a closer destination") 