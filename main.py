def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return f(n // 2)
k = 0
for z in range(1000000000):
    if f(z) == 2:
        k += 1
        print(k, z)