def listnumber(items):
    for i in items:
        if i > 20:
            items.remove(i)

    return items


print(listnumber([1,210,22,121,13,434,0,12]))
