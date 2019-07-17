
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



db = {}
while True:
    command = input()
    command_list = command.split()
    if command_list[0] == "ADD":
        pass
    elif command_list[0] == "COUNT":
        pass
    elif command_list[0] == "EXIT":
        break
