N = int(input("Enter limit: "))
a = 0
b = 1
while a < N:
    print(a)
    a, b = b, a + b
