lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = lst.copy()
for i in new_lst:
    if i == 0:
        new_lst.remove(0)
        new_lst.append(0)
print(lst)
print(new_lst)