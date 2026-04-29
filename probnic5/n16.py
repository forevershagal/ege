def f(n):
    if n > 4000:
        return n
    else:
        return f(n+2) * 3 + 5 * n

print(f(3988)//f(3998))