import sys

sys.stdout.write("Hello")

while True:
    line = input()  # При окончании ввода (Ctrl+D / Ctrl+Z) → EOFError
    print(line)
