import sys

while True:
    char = sys.stdin.read(1)  # Читает ровно 1 символ
    if not char:              # EOF → пустая строка
        break
    print(f"Символ: {char!r} (код: {ord(char)})")