"""
    A calculator function from malikchika86@gmail.com
"""
def calculator(a, operator, b):
        if operator =='*':
            return a * b
        if operator == '+':
              return a + b
        elif operator == '-':
              return a - b
        elif operator == '/':
              return a / b
        elif operator == '√':
              return a ** b
            

"""
    Test cases
"""
multiplication = calculator(3, '*', 4)
addition = calculator(4, '+', 4)
subtraction = calculator(4, '-', 4)
division = calculator(4, '/', 4)
square = calculator(4, '√', 4)


test = [multiplication, addition, subtraction, division, square]
for i in test:
      print(i)
