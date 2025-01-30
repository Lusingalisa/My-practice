## LISTS
#number =[1, 5, 7, 8, 3]
#sum = len(number)
#print(f"The sum of numbers is {sum}")

# numbers =[8, 7, 6, 2, 9]
# product = 1
# for number in numbers:
#     product *= number
# print(f"The product of all items in the list is {product}") 

# my_list =[2,5,7,9,4]
# product = 1
# for i in my_list:
#     product *= i
# print(f"The product is {product}") 

# numbers = [1,3,7,5,8,9,23,87]
# largest = max(numbers)
# print(f"the largest is {largest}") 
        #OR
# numbers = [3,6,18,7,9,2]
# largest_num =numbers[0]
# for number in numbers:
#     if number > largest_num:
#         largest_num = number
# print(f"the largest number is {largest_num}")

# numbers = [56,37,21,17,5,2]
# smallest = min(numbers)
# print(f"The smallest number is {smallest}") 

# samples = ['abc','xyz','aba','1221']
# count = 0
# for sample in samples:
#     if sample[0] == sample[-1]:
#         count += 1
# print(f"The number of strings with the same first and last characters is {count}")

# tuples_list = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# sorted_list = sorted(tuples_list, key=lambda x: x[-1])
# print(f"Sorted list by the last element of each tuple: {sorted_list}")

# def remove_duplicates(lst):
#         return list(set(lst))
# my_list = [1,3,6,4,1,2,5,3]
# unique_list = remove_duplicates(my_list)
# print(unique_list)
## Or: using loops
# def remove_duplicates(lst):
#         seen=[]
#         unique_list=[]
#         for item in lst:
#                 if item not in seen:
#                         seen.append(item)
#                         unique_list.append(item)
#         return unique_list
# my_list =[1,3,6,5,1,2,7,5]
# unique_list=remove_duplicates(my_list)
# print(unique_list)
## append adds things/items to the end of a list and lst represents a list
## we start by creating an empty list called seen which is going to hold the duplicated values.
## we create another empty list called unique_list that'll take the unique items.
## so if the item doesn't appear in seen, we add it to the seen and uniquelist using the append function.

# def is_list_empty(lst):
#         if not lst:
#                 return True
#         else:
#                 return False
# mylist1 =[]
# mylist2 =[1,3,5,8]
# print("Is my list 1 empty?", is_list_empty(mylist1))
# print("Is my list 2 empty?", is_list_empty(mylist2)) 

# def clone_list(original):
#         clone1=list(original)
#         return clone1
# my_list = [1,2,3,4,5]
# clone1=clone_list(my_list)
# print("original list: ", my_list)
# print("a copy:", clone1)

# def clone_list(original):
#     # Method 1: Using the list() function
#     clone1 = list(original)

#     # Method 2: Using the copy() method
#     clone2 = original.copy()

#     # Method 3: Using slicing
#     clone3 = original[:]

#     return clone1, clone2, clone3

# # Example usage
# my_list = [1, 2, 3, 4, 5]

# clone1, clone2, clone3 = clone_list(my_list)

# print("Original List:", my_list)
# print("Clone using list():", clone1)
# print("Clone using copy():", clone2)
# print("Clone using slicing:", clone3) 

# my_list=[1,2,3,4,5]
# a,b,c,d,e = my_list
# print("a:",a)
# print("b:",b)
# print("c:",c)
# print("d:",d)
# print("e:",e) 

# num=[1,3,5,4,2,6]
# count=0
# for i in num:
#         count+=i
# print(f"The sum is {count}")        

# sample_list=[8,2,3,-1,7]
# product = 1
# for num in sample_list:
#         product *= num
# print(f"The product is {product}")

# def reverse_string():
#         sample="1234abcd"
#         sample=sample[::-1]
#         return sample
# print("The sample is ",reverse_string())

# def factorial(n):
#         if n<0:
#                 return ValueError("Factorial for negative values is not defined.")
#         elif n==0 or n==1:
#                 return 1
#         else:
#                 result = 1
#                 for i in range(2,n+1):
#                         result*=i
#                 return result
# number = int(input("Enter a number: "))
# print(f"The factorial of {number} is {factorial(number)}")

# def remove_duplicates(lst):
#         return list(set(lst))
# sample=[1,3,5,2,1,3]
# print(f"The unique_list is {remove_duplicates(sample)}")

# def is_in_range(number,start,end):
#         return start <= number <= end
# num =int(input("enter a number: "))
# range_start= 3
# range_end= 8
# if is_in_range(num,range_start,range_end):
#         print(f"{num} is in range")
# else:
#         print(f"{num} is not in range") 

# for x in range(1,7):
#     for y in range(1,7):
#         print(f"{x}*{y} = {x*y}") 

# secret_number=8
# while True:
#         number = int(input("Enter a number bewteen 1 and 20: "))
#         if number == secret_number:
#                 print("You got it right!")
#                 break
#         elif number< secret_number:
#                 print("Your guess was too low")
#         else:
#                 print("Your guess is too high") 

# for i in range(11):
#         if i==4 or i==8:
#                 continue
#         print(i) 

# for i in range(5):
#         if i ==2:
#                 pass
#         else:
#                 print(i) 

# input_string="green-red-yellow-black-white"
# words= input_string.split('-')
# words.sort()
# sorted_string='-'.join(words)
# print(f"Sorted string: {sorted_string}") 

# def remove_duplicates(lst):
#         seen=[]
#         unique_list=[]
#         for i in lst:
#                 if i not in seen:
#                         seen.append(i)
#                         unique_list.append(i)
#         return unique_list
# numbers = [1,3,4,1,2,3,5]
# unique_list=remove_duplicates(numbers)
# print(f"The unique list is {unique_list}")

# fruits=["apple","banana","apricot","cherry"]
# removed=fruits.pop()
# print(f"Processed:{fruits}")

# fruits = ['apple','banana','coconut','watermelon','nirvana','mango']
# count = 0
# for item in fruits:
#         if item[0]==item[-1]:
#                 count+=1
# print(f"The number of strings with same first and last characters is {count}")

# for i in range(1,31):
#         print(f"The square of {i} is {i**2}")

# def second_largest(lst):
#         unique_elements=list(set(lst))
#         unique_elements.sort(reverse=True)
#         if len(unique_elements)>1:
#                 return unique_elements[1]
#         else:
#                 return None
# numbers = [10,20,5,15,7,8]
# result= second_largest(numbers)
# print(f"the 2nd largest is {result}")

def months_to_pay():
        time=20000000/1500000
        print(f"It will take Michael {time} months to pay ")

months_to_pay()
