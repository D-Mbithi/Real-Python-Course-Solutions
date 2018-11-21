def list_number(lists):
    new_list = []
    for i in lists:
        if i >= 20:
            new_list.append(i)
    return new_list

print(list_number([2,3,4,21,23,12,32,12,31,12,12,14,115])
