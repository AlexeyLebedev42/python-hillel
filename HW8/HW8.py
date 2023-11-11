lst = [1, 3, 5]
print(lst)
sum = 0
a = lst[::2]
if lst:
    for i in a:
        sum = sum + i
    sum = sum * a[-1]
print(sum)