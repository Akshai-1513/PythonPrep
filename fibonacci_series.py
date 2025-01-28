n = int(input("Enter the number: "))
a, b = 0, 1
for _  in range(n):
    a, b = b, a+b # Here we add the the value of a and b to get the next value
    print(b, end = " ")
