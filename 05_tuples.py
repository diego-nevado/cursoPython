### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.83, "Diego" , "Nevado", "Diego")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Diego"))
print(my_tuple.index("Nevado"))
print(my_tuple.index("Diego"))

#my_tuple[1] = 1.86 'tuple' object does not support item assigment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "NevaByte"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

