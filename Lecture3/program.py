
#База должна хранить в себе года, когда человек изменял свое ФИ.
#У базы есть 4 внешних  метода(функции):

#ADD year name surname id ---> добавить человека с id в базу
#В случае, если id свопадает --- считать, что это один и тот же человек.

#COUNT year  id ---> все изменения ФИ  у человека с данным id
#COUNT 1933 1 --->> 1922 (Игорь, Николаев) ---1928 (Игорь, Залюбовь)

#LOGOUT ---> печать в текстовый файл
#id1 year1,name1,surname1 ---- year2,name2,surname2----...----yearN,nameN,surnameN
#id2 ....

#EXIT --> exit
#В случае, если изменений не было или они не требуются : ставим "!"

#Example:

#Input:                                 #Output
#ADD 1922 Vasiya Pupkin 1
#ADD 1932 Anna Bah 2
#ADD 1955 Vasiliy ! 1
#ADD 1973 !  Pupkinsky 1
#COUNT 1                                2
#COUNT 2                                0

def add_to_db(db, list_to_add):
    id_user = list_to_add[-1] #THis is magic id -- int
    data_line = list_to_add[:3] #Inner: [year,name,surname]
    if id_user in db.keys():
        if "!" in data_line:
            pos = data_line.index("!")
            data_line[pos] = db[id_user][-1][pos]
        db[id_user].append(data_line )
    else:
        db[id_user] = [data_line ]

    return db

def count_changes(db, year, ids):
    dump = []
    for v in db[ids]:
        if v[0] < year:
            dump.append(v)
    return dump


def logout(db):
    file_name = "log_file.txt"
    with open(file_name, "a") as f:
        for k,v in db.items():  #k    y n s    y n s    y n s
            string_to_write = "%s "%k
            for val in v:
                string_to_write+= "    "
                for word in val:
                    string_to_write+= (word+" ")

            f.writelines(string_to_write)
            f.write("\n")


    



db = {}
while True:
    command = input()
    command_list = command.split()
    if command_list[0] == "ADD":
        db = add_to_db(db,command_list[1:])
        print(db)
        
    elif command_list[0] == "COUNT":
        t = count_changes(db, command_list[1], command_list[-1])
        print(t)
    elif command_list[0] == "LOGOUT":
        logout(db)
    elif command_list[0] == "EXIT":
        break


