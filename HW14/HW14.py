user_number = int(input("Please enter  number:"))

while user_number > 9:
   multiple = 1
   user_number = str(user_number)
   for i in user_number:
      multiple = int(i) * multiple
      print(multiple)
      user_number = multiple
print("Result: ", user_number)