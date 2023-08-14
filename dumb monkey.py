input_str = input()
maxn = 0
minn = 101
for i in range(0, len(input_str)):
    if maxn < input_str.count(input_str[i]):
        maxn = input_str.count(input_str[i])

for i in range(0, len(input_str)):
    if minn > input_str.count(input_str[i]):
        minn = input_str.count(input_str[i])

num = maxn - minn

k = 2
tf = True

if num == 0 or num == 1:
    print("No Answer")
    print("0")
    exit()
if num == 2 or num == 3:
    print("Lucky Word")
    print(num)
    exit()

while k < num:
    if num % k == 0:
        tf = False
        break
    k += 1

if tf:
    print("Lucky Word")
    print(num)
else:
    print("No Answer")
    print("0")
