obj_persons = {}
keys = ['1','2','3']
keys_n = ['a','s','d','f']
for key in keys:
    obj_persons[key] = {}
    index = 4
    for k in keys_n:
        obj_persons[key][k] = index
        index += 1


print(obj_persons)