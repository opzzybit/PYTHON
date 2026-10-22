employees_list = [
("John", "IT", 50000),
("Jane", "HR", 45000),
("Mike", "IT", 60000),
("Sara", "Finance", 70000)]


for names,departments,salary in employees_list:
    print(names,departments,salary)

for names,departments,salary in employees_list:
    if departments == "IT":
        print(names,departments)
        
for names,departments,salary in employees_list:
    if salary > 55000  :
        print(names,salary)
