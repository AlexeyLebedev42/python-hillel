import random
list1 = []
list2 = []
def common_elements():
    for i in range(random.randint(10,100)):
        if i % 3 == 0:
            list1.append(i)
        else:
            pass
    print(list1)
    for i in range(random.randint(10,100)):
        if i % 5 == 0:
            list2.append(i)
        else:
            pass
    print(list2)
    set_1 = set(list1)
    set_2 = set(list2)
    set_common = set_1.intersection(set_2)
    return set_common
print('Перетин множин:', common_elements())