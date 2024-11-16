my_dict={"Svetlana": 1999, "Daniil": 2007, "Mari": 2015}  # №2 Словари и множества
print("Dict: ", my_dict)
print(my_dict.get("Daniil"))
print(my_dict.get("Anna", "Такого ключа нет"))
my_dict.update({"Nika": 2005, "Viktor": 1980})
print(my_dict)
a=my_dict.pop("Mari")
print("Deleted value:", a)
print("Modified dictionary:", my_dict)

my_set={1,"Name",3,3,2,3,5,6} #№ 3 Словари и множества
print(my_set)
my_set.update({88,9})
print(my_set)
my_set.discard(3)
print(my_set)
