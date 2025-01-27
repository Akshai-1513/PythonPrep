import time
def prime_number(n):
    for i in range(2, int(n**0.5) + 1): # This will iterate till certain value
        if n % i == 0: 
            return False
    return True

num = int(input("Enter the number: "))

if prime_number(num):
    print("The given number is prime number ")
else:
    print("The is number is not a prime number")

time.sleep(2)
