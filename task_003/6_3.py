# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def sort_list(persons):
    print(persons)
    keys = [i[0] for i in persons]
    obj_persons = {}

    for key in keys:
        obj_persons[key] = [i for i in persons if i[0] in key] 
    obj_persons_sort = dict(sorted(obj_persons.items()))

    return obj_persons_sort            


persons = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
print(sort_list(persons))