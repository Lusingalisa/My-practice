""""Qn1: Even Odd Checker(3marks): Write a python program that asks the user to enter a number and then displays whether the number is even or odd"""
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd") 

""""Qn2: Reverse String (4 marks): Write a program that reverses a given String. (For example, Boy becomes yoB)."""
sample="Boy"
reversed_string = sample[::-1]
print(f"Reversed string is {reversed_string}")

"""Qn3: Multiplication table (6 marks): Write a Python program to print the multiplication table up to 6×6. The output should display each multiplication in the format a * b = result for values of a and b from 1 to 6."""
for i in range(1,7):
    for j in range(1,7):
        multiplication = i * j
        print(f"{i}*{j} = {multiplication}") 

"""Qn4: FizzBuzz (6 marks): Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz"."""
for i in range(1,101):
    if i%3 == 0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    elif i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    else:
        print(i) 

"""Qn5: Maximum (7 marks): Write a python function to find the maximum of 3 given numbers. Use parameter passing and a return statement."""
def max_of_numbers(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num3:
        return num2
    else:
        return num3
number1 = 5
number2 = 20
number3 = 15
maximum = max_of_numbers(number1,number2,number3)
print(f"The maximum number is {maximum}") 

"""Qn6: Print numbers (4 marks): Write a Python program that prints all the numbers from 0 to 10 except 4 and 8. Note: Use 'continue' statement. Expected Output : 0 1 2 3 5 6 7 9 10."""
for i in range(11):
    if i==4 or i==8:
        continue
    print(i)
