import random
list = []

for i in range(random.randint(3, 10)):
    list.append(random.randint(1, 10))
print(list)
a = list[0]
b = list[2]
c = list[-2]

new_list = [a, b, c]
print(new_list)