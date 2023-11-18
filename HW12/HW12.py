import string
user_string = input('Введить бажаний рядок:')
list = []
print(user_string)
for i in user_string:
    if i not in string.punctuation:
        list.append(i)
        hashtag = ''.join(list)

hashtag = hashtag.strip()
hashtag = hashtag.title()
hashtag = ''.join(hashtag.split())
hashtag = '#' + hashtag[:139]

print(hashtag)