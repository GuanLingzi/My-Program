# addition, subtraction, multiplication and division
class OperatorError(Exception):
    pass


def addition(n1, n2):
    s = n1 + n2
    return s


def subtraction(n1, n2):
    s = n1 - n2
    return s


def multiplication(n1, n2):
    s = n1 * n2
    return s


def division(n1, n2):
    s = n1 / n2
    return s


while True:
    try:
        in_l = input('Please enter the formula at one time (e.g.:1 + 2)：').split()
        num1, num2 = int(in_l[0]), int(in_l[2])
        if in_l[1] == '+':
            print('Calculation results：', addition(num1, num2))
        elif in_l[1] == '-':
            print('Calculation results：', subtraction(num1, num2))
        elif in_l[1] == '*':
            print('Calculation results：', multiplication(num1, num2))
        elif in_l[1] == '/':
            print('Calculation results：', division(num1, num2))
        else:
            raise OperatorError('What you entered at the second character is not an operator')
    except (ValueError, ZeroDivisionError) as e:
        print(e)
        print('Please enter again')
    except Exception as e:
        print(e)
    else:
        break
