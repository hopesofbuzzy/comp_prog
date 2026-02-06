alphabet_example = "1ij2abc3def4gh5kl6mn7prs8tuv9wxy0oqz"
alphabet = {}
num = ""
for c in alphabet_example.replace("\n", "").replace(" ", ""):
    if c.isdigit():
        num = c
    else:
        alphabet[c] = num


def find_line(num, n, words) -> str:
    passed_positions = []
    queue = [((), ())]  # (строка, числовое_обозначение_строки)
    while queue:
        node = queue.pop(0)
        for word, word_num in words.items():
            used_words = node[0] + (word,)
            used_words_num = node[1] + (word_num,)
            line_num = "".join(used_words_num)
            if line_num != num[:len(line_num)]:
                continue
            pos = len(line_num)-1
            if pos in passed_positions:
                continue
            passed_positions.append(pos)
            if len(line_num) < len(num):
                queue.append((used_words, used_words_num))
            elif len(line_num) == len(num):
                if line_num == num:
                    return " ".join(used_words)
    return "No solution."


def get_words_dict(words) -> dict:
    new_words = {}
    for word in words:
        new_words[word] = "".join(alphabet[c] for c in word)
    return new_words


while True:
    num = input()
    if num == "-1":
        break
    n = int(input())
    words = tuple(sorted((input() for _ in range(n)), key=len))
    words = get_words_dict(words)
    print(find_line(num, n, words))
