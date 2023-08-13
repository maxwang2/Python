k = int(input())
lst = []
n = 1
a = 1
sum = 0
lst.append(n)
while len(lst) < k:
    if n == 1:
        n = 2
        lst.append(n)
        continue
    if a == n:
        n += 1
        a = 1
        lst.append(n)
    else:
        a += 1
        lst.append(n)
for i in lst:
    sum += i

print(sum)
