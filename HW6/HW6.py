lst = [12, 3, 4, 10, 8]
print(lst)
if len(lst) < 1:
    print([])
else:
    z = lst[-1]
    lst.pop()
    lst.insert(0, z)
    print(lst)

