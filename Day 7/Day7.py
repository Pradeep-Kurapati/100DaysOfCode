from art import logo

print(logo)

# Adding
def add(n1, n2):
  '''This function returns sum of it's arguments. '''
  return n1+n2

# Subtract
def subtract(n1, n2):
  '''This function returns difference between it's arguments. '''
  return n1-n2

# Multiply
def multiply(n1, n2):
  '''This function returns product of it's arguments. '''
  return n1*n2

# Division
def divide(n1, n2):
  '''This function returns division of it's arguments. '''
  return n1/n2

# Creating a dictionary

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}
# Creating a function for calculator.
def calculator():
  stop = False
  num1 = int(input("Enter first number: "))
  for x in operations:
      print(x)
  #Taking input
  while stop == False:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("Enter second number: "))
    ans = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {ans}")
    num1 = ans
    choice = input(f"Type y to continue calculating with {ans}, type n to start new calculation..")
    if choice == 'n':
      stop = True
      calculator()

calculator()