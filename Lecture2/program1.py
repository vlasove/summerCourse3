num = []
start = 1
end = 1000

i = start
while i <= end:
    num.append(i)
    i+=1


sum_of_elem = 0
mult_of_elem = 1

j = 0
while j < len(num):
    if num[j]%2==0:
        sum_of_elem+=num[j]
    else:
        mult_of_elem*=num[j]

    j+=1

print("The total sum is : %i\nTotal mult is: %i"%(sum_of_elem,mult_of_elem))


#1) Сумма всех четных (по значению) элементов в списке num
#2) Проивзедение всех нечетных (по значению) элементов в списке num
