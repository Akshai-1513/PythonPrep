num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10 # We get the remainder value to to cube the value
    sum += digit ** 3 # The cube value is added the other values 
    temp //= 10 # This will get the quotient value 
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
