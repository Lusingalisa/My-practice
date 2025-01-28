def is_palindrome(s):
    # Normalize the string
    #The  goal is to clean the string in order to only contain lowercase letters and numbers.
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the original string is equal to the reversed string.
    return normalized == normalized[::-1]

# Main program
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
