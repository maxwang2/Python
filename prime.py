num = int(input())
k = 2
tf = True

if num == 1:
    print("No")
    exit()
if num == 2 or num == 3:
    print("Yes")
    exit()

while k < num:
    if num % k == 0:
        tf = False
        break
    k += 1

if tf:
    print("Yes")
else:
    print("No")
