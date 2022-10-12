# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def sort_list(persons):
    print(persons)
    keys = []
    for i in persons:
        if not i[0] in keys:
            keys.append(i[0])

    # keys = [i[0] for i in persons if not i[0] in keys]
    
    obj_persons = {}
    temp = []
    for key in keys:
        for i in persons:
            if i[0] in key:
                temp.append(i)
        obj_persons[key] = temp
        temp = []
    obj_persons_sort = dict(sorted(obj_persons.items()))

    return obj_persons_sort            


persons = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
print(sort_list(persons))