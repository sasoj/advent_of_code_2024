import lib
alist = []
blist = []
for a, b in lib.int_records(1):
    alist.append(a)
    blist.append(b)
alist.sort()
blist.sort()
sum = 0
for a, b in zip(alist, blist):
    x = a - b
    sum += max(x, -x)
    

print(sum)

score = 0
for a in alist:
    score += a * blist.count(a)

print(score)