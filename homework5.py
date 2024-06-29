immutable_var = 1, 2, "абв", "где", True
print(immutable_var)
# кортеж  - неизменяемый объект, не поддерживающий обращение по элементам. Изменить данные в кортеже
# можно если в нём есть список или посредством сложения/умножения
immutable_var = immutable_var + (3, 4, "жзи", "клм", False) #пример 1
print(immutable_var)
immutable_var = ([1, 2], 3, "абв")
print(immutable_var)
immutable_var[0][0] = 6 #пример 2
print(immutable_var)

mutable_list = ["Иванов", "Петров", "Сидоров"]
print(mutable_list)
mutable_list[0] = "Соловьёв"
mutable_list[1] = "Смирнов"
mutable_list.append("Васильев")
print(mutable_list)