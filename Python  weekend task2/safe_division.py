PYTHON

print("welcome to a calculator called, safe division ")

boxes = int(input("Enter  number of boxes :  "))
tables = int(input("Enter number of tables :  "))

result = boxes / tables
print("result is ", result)

if result != 0:
  print("cannot divide by zero")
