# try:
#     a = 20
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print('There is a divide by zero error')
# finally:
#     print('This is going to execute no matter what')

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("There is a divide by zero error")
        return 0


x = float(input('Enter a number : '))
y = float(input('Enter value by which you want to divide the number : '))
print(divide(x, y))
