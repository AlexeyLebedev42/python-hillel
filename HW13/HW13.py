import string

str = string.ascii_letters
user_string = input('Введіть через дефіс дві літери:')

index1 = str.index(user_string[0])
index2 = str.index(user_string[2])
result = str[index1:index2+1]
print(result)

