def duplicate(name_1, name_2):
    for i in name_1:
        if i in name_2:
            name_2.remove(i)

    name_1.extend(name_2)
    return (name_1)


a = duplicate(['sagar', "riya", "sayani"], ["monami", "sagar"])
print(a)