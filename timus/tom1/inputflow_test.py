import sys

# Ответ после ввода всех строк (^+Z+Enter)
lines = sys.stdin.readlines()
print('This is a line: ', lines)

# Мгновенный ответ после ввода строки
for line in sys.stdin:
    print(line[:-1])

# Получение всех элементов вне зависимости от количества пробелов или переносов
print(sys.stdin.read().split())

sys.stdout.write("Hello")