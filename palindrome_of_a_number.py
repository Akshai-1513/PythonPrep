num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10  # The remaindeer value is added to the rev value
    num //= 10
print("Reversed number:", rev)

if num == rev:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")