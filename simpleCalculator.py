# Declare the the first memeber of the operation
print("Enter the first argument")
x = int(input())

# Declare operation
print("Enter the operation")
op = str(input())

# Declare the the first memeber of the operation
print("Enter the second argument")
y = int(input())

if op == "+":
  z = x + y
elif op == "-":
  z = x - y
elif op == "*":
  z = x * y
elif op == "/":
  try:
    z = x / y
  except ZeroDivisionError:
    z = "Not defined or infinity"
else:
  z = "The operation is not valid!"

print(z)
