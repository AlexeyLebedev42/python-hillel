x = [1, 2, 3, 4, 5, 6]
i = int((len(x) + 1) / 2)
k = int(len(x) / 2)
if len(x) % 2 == 0:
    print([x[0:k], x[k:]])
else:
    print([x[0:i], x[i:]])
