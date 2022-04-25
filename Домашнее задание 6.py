# Задание 1. Распарсить. Получить списки кортежей

with open("file.txt", "r", encoding="utf-8") as file_1:

    for line in file_1:
        my_list = []
        content = file_1.readline()
        remote_addr = content[:content.find(' ')]
        request_type = content[content.find('"')+1: content.find('"') + 4]
        requested_resourse = content[content.find('/d')+1:content.find('HTTP')]
        all_i_need = (remote_addr, request_type, requested_resourse)
        my_list.append(all_i_need)
        my_tuple = tuple(my_list)
        print(my_tuple)


# Задание 3. ФИО и хобби

hobby = open("hobby.txt", "r", encoding="utf-8")
names = open("names.txt", "r", encoding="utf-8")

hobby_and_names = {}

for line, name in zip(hobby, names):

    hobby_and_names[name] = line.splitlines()

print(hobby_and_names)
a = str(hobby_and_names)

hobby.close()
names.close()

# Задание 6

# Проработал, но не вижу смысла сдавать код из вебинара






