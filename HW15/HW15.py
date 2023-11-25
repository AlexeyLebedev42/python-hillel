user_input = int(input("Введіть число, яке більше або дорівнює 0 і менше ніж 8640000:"))

if user_input >= 0 and user_input < 8640001:
    minutes = int(user_input / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)

    converted_hour = int(user_input / 60 / 60) - (days * 24)
    converted_hour = str(converted_hour).zfill(2)

    converted_minutes = int(user_input / 60) - (hours * 60)
    converted_minutes = str(converted_minutes).zfill(2)

    converted_sec = user_input - int(minutes * 60)
    converted_sec = str(converted_sec).zfill(2)
    ending = ''
    if days % 10 == 1 and days != 11:
        ending = 'день'
    elif 2 <= days % 10 <= 4 and days != 12 and days != 13 and days != 14:
        ending = 'дні'
    else:
        ending = 'днів'
    print(f"{days} {ending}, {converted_hour}:{converted_minutes}:{converted_sec}")
else:
    print('Ви ввели не вірне число!')
