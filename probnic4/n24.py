f = open('/Users/shagal/Desktop/shagalievv/Школково/Информатика/tasks/24__a7x9e.txt')
s = f.readline()
gl = "AEIOUY"
start = gl_count = tw_count = 0
mn = 10 ** 10
for end in range(len(s)):
    if s[end] in gl:
        gl_count += 1
    if s[end - 1: end + 1] == "20":
        tw_count += 1

    while tw_count >= 26 and s[end] in gl:
        if gl_count == 1 and tw_count == 26:
            mn = min(mn, end - start + 1)

        if s[start] in gl:
            gl_count -= 1
        if s[start: start + 2] == "20":
            tw_count -= 1
        start += 1  # сдвигаем левый указатель
print(mn)

