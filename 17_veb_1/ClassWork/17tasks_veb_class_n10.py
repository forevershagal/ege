f = open('D:/INC/task17_veb1_class/10.txt')

a = [int(i) for i in f]

mx821 = max(i for i in a if str(i)[-3:] == '821')
mn821 = min(i for i in a if str(i)[-3:] == '821')
s821 = 2 * (mx821 + mn821)
c = 0
mx = -1000000000000000000000000

for i in range(len(a) - 3):
    t = [a[i], a[i+1], a[i+2], a[i+3]]

    p5 = len([g for g in t if 10000 <= g <= 99999])
    p3 = len([g for g in t if 100 <= g <= 999])

    m5 = len([x for x in t if x % 5 == 0])
    m7 = len([x for x in t if x % 7 == 0])

    if (p5 > p3) and (m5 == m7) and (sum(t) > s821):
        c += 1
        mx = max(mx, sum(t))

print(c, mx)