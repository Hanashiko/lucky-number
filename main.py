def factorial(n):
    a = 1
    for i in range(n + 1, n + 10):
        a *= i
    return a

fact = 1
for i in range(2, 10):
    fact *= i

n = int(input())
print(factorial(n) // fact)
