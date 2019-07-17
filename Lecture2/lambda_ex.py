def Summer(a,b):
    return a+b

a = Summer
print(a(2,3) )


he = lambda x,y: x+y
print(he(2,3))
q = ["lol", "kek", "pep"]
f = lambda v : [" " for i in q] 
q = f(q)
print(q)

#["lol", "kek", "pep"] --->lambda ---> [" ", " ", " "]


names = {"Derek": 31, "John":23, "Peter": 15, "Francisca":40}
#year ->lambda names: --> year+1

my_lambda = lambda names: {k:names[k]+1 for k in names.keys()}
print(names)
names = my_lambda(names)
print(names)