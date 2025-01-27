n = int(input("Enter the number: "))
a, b = 0, 1
for _  in range(n):
<<<<<<< HEAD
    a, b = b, a+b # Here we add the the value of a and b to get the next value
    print(b, end = " ")
=======
    print(a, end = " ")
    a, b = b, a + b
>>>>>>> f4e2406cda9f77ac143d426e70138c072f3c1d5b
