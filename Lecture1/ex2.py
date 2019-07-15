#Реализуйте хранилище данных следующего вида.
#У вас есть 2 команды :
#1) ADD name1,name2,name3,name4 .....
#2) COUNT name 
#3) EXIT

#input                      #output
#ADD Ruben, Maxim
#ADD Ruben, Oleg
#COUNT Ruben                2
#COUNT Oleg                 1
#COUNT Vasya                Who is it?
data_base = []

data_base = [["Sara", 2], ["Kira", 10], ["Ruben", 5000000]]
while True:
    command = input("Enter command: ")
    list_of_command = command.split()
    if list_of_command[0] == "ADD":
        #print(list_of_command[1])
        names = list_of_command[1].split(',')
        #print(names)
        
    elif list_of_command[0] == "COUNT":
        pass
    elif list_of_command[0] == "EXIT":
        break
print(data_base)