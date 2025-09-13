input_string = input("Enter the string: ")
reversed_string = "" # Empty string is initialized 

for char in input_string:
    reversed_string = char + reversed_string # The character is appended at the front of the character
print("The reversed string is ",reversed_string)

if input_string == reversed_string:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")
