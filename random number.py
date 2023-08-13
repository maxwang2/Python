amount = int(input())
lst = []
times = 1
while amount != 0:
    flag = True
    current_num = int(input())
    if times == 1:
        lst.append(current_num)
        amount -= 1
        times += 1
        continue
    for i in range(0, len(lst)):
        if lst[i] == current_num:
            amount -= 1
            flag = False
            break
    if flag:
        lst.append(current_num)
        amount -= 1

lst.sort()
print()
print(len(lst))
for i in lst:
    print(i, end=" ")
