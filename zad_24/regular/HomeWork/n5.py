from re import *

s = open('D:/INF_tasks/task24_reg/24_2__6jwgo.txt').readline()

mx = 0
mxln = 0
st = ''
num = r'([789][0789]*)'
reg = rf'{num}([-*]{num})*'

for i in finditer(reg, s):
    res = i.group()
    if '-' in res or '*' in res:
        if len(res) > mxln:
            mxln = len(res)
            st = res

answer = str(abs(eval(st)))[:6]
print(answer)
