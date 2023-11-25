user_number = int(input("Please enter  number:"))

while user_number > 9:
   multiple = 1
   user_number = str(user_number)
   for i in user_number:
      multiple = int(i) * multiple
      print(multiple)
      user_number = multiple
print("Result: ", user_number)


























# user_number = int(input("Please enter  number:"))
# i = 0
# multiple = 1
# string = str(user_number)
# # do = len(string)
#
# while len(string) > 1:
#    multiple = multiple * (user_number % 10)
#    user_number = int(user_number // 10)
#    i = i + 1
#    if i == len(string):
#        if (multiple > 9):
#            user_number = multiple
#            multiple = 1
#            i = 0
#            string = str(user_number)
#            # do = len(string)
#        else:
#            break
#
# print("Результат: ", multiple)