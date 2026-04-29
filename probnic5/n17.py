mn = 10**10
c = 0
path = '/Users/shagal/Downloads/10__1vf5g.txt'
f = open(path)
a = [int(i) for i in f]
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if ((a[i] - a[j]) % 2 == 0) and (a[i] % 11 == 0 or a[j] % 11 == 0):
            c += 1
            mn = min(mn, a[i]+a[j])
print(c, mn)