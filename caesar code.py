lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = int(input())
code = list(input())
for i in range(0, len(code)):
    index = lst.index(code[i])+n
    code[i] = lst[index]
for i in code:
    print(i, end="")
