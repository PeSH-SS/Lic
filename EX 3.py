def fibonacci(n):
    a = 0
    b = 1;
    print(a)
    for i in range(0,n+1):
        c = a
        a = b
        b = a + c
        print('fib(',i,')=',c)

