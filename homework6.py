my_dict = {"Игорь": 2000, "Антон": 1997, "Семён": 1999, "Павел": 2004, "Сергей": 1994}
print(my_dict)
print(my_dict["Антон"])
print(my_dict.get("Кирилл"))
my_dict.update({"Евгений": 2001, "Вячеслав": 2002})
a = my_dict.pop("Игорь")
print(a)
print(my_dict)

my_set = {1, 2, "Слова", 3, "Буквы", 2, "Цифры", 1, 3, 4, 2, "Слова", "Цифры", 2, 1, "Буквы", 5}
print(my_set)
my_set.add(6)
my_set.add("Предложения")
my_set.discard("Цифры")
print(my_set)
