for x in range(11110, 55557):
    c = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            c.add(i)
            c.add(x//i)
    if len(c) == 3:
        print(*sorted(c))