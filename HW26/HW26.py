def is_even(number):
    number = str(number)
    if number[-1] != "1" and number[-1] != "3" and number[-1] != "5" and number[-1] != "7" and number[-1] != "9":
        return True
    else:
        return False



assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'