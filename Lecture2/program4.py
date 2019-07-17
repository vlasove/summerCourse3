empty_dict = {}
empty_dict_2 = dict()

print(type(empty_dict))

empty_dict = {"one":1, "two":2,"three":3}
empty_dict["zero"] = 0
print(empty_dict)

names = {"Nikolay":10, "Margo":15}
list_of_names = ["Andrey","Andrey","Margo", "Andrey", "Nikolay"]

for item in list_of_names:
    if item in names.keys():
        names[item] +=1

    else:
        names[item] = 1

print(names)


