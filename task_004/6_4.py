# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

def sort_dist(persons):
    keys_surname = []
    keys_name = []
    for person in persons:
        p = person.split()
        for i in range(len(p)):
            if i == 1:
                item = p[i]
                if not item[0] in keys_surname:
                    keys_surname.append(item[0])

    for i in persons:
        if not i[0] in keys_name:
            keys_name.append(i[0])
    # keys_name = [i[0] for i in persons if not i[0] in keys_name]
    
    obj_persons = {}
    
    print(persons)
    for key in keys_surname:
        obj_persons[key] = {}
        for k in keys_name:
            temp = []
            for person in persons:
                person = person.split()
                if  k in person[0] and key in person[1]: 
                    person = ' '.join(person)
                    temp.append(person)
                    obj_persons[key][k] = (temp)
                   
    print(obj_persons)


string = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",\
     "Анна Савельева", "Юнона Ветрякова",\
        "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
sort_dist(string)

