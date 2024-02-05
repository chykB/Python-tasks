""" 
    User input for 2 number and operators
"""
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
operator = input('Select: + for addition, - for subtraction, * for multiplication, / for division: ')

"""
Perform operation on numbers and display the result
"""
if operator == '+':
    result = a + b
    print(f"{result}")
elif operator == '-':
    result = a - b
    print(f"{result}")
elif operator == '*':
    result = a * b
    print("{result}")
elif operator == '/':
    result = a / b
    print(f"{result}")
else:
    print("Invalid! Please select a valid operator")