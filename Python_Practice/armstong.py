def armstrong(num):
    length = len(str(num))  # Correct way to get number of digits
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10
    if sum == num:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

n = int(input("Enter the number: "))
print(armstrong(n))