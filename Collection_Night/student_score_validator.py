main_list = [("Alice", 78),
             ("Bob",   45),
             ("Charlie",90),
             ("Diana",  62),
             ("Kent",   30)]

print()
print ("NAMES      SCORES")
for name,scores in main_list:
   print()
   print(f"{name}         {scores}", end= "\n")

print()
print("STUDENT GREATER THAN OR EQUAL TO 60")
for name,scores in main_list:
    if scores >= 60:
        print(name)


print()
print("AMOUNT OF STUDENT THAT PASSED")
count = 0
for name,scores in main_list:
    if scores >= 50:
        count += 1
print(f"the amount = {count} students")

