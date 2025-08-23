#calculator including functions, try,except, while loops and if statements

def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid number, try again. ")



operand = get_number(1)
operand2 = get_number(2)
sign = input( "Sign: ")


try:
    operand = float(operand)
    operand2 = float (operand2)
except: 
    print("Invalid operands. ")

result = 0
if sign == "+":
    result = float(operand) + float(operand2)
elif sign == "-":
    result = float(operand) - float(operand2)
elif sign == "/":
    result = float(operand) / float(operand2)
    if operand2 != 0:
        result = operand / operand2
    else:
         print("Division by zero. ")
elif sign == "*":
    result = float(operand) * float(operand2)
print(result)


