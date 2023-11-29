def difference(*args):
    if args != ():
        max_number = max(args)
        min_number = min(args)
        difference = max_number - min_number
        difference = round(difference, 2)
        return difference
    else:
        return 0
    print(difference(*args))


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')