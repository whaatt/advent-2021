# mypy: ignore-errors
# flake8: noqa

data = open("10-input.txt").read()
data = data.split("\n")[:-1]

# data = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]

score_map = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

for line in data:
    bad = False
    char_stack = []
    for char in line:
        if char in "([{<":
            char_stack.append(char)
        else:
            if char == ")" and ((not char_stack) or char_stack[-1] != "("):
                bad = True
                break
            if char == "]" and ((not char_stack) or char_stack[-1] != "["):
                bad = True
                break
            if char == "}" and ((not char_stack) or char_stack[-1] != "{"):
                bad = True
                break
            if char == ">" and ((not char_stack) or char_stack[-1] != "<"):
                bad = True
                break
            char_stack.pop()
    if bad:
        continue
    score = 0
    for char in char_stack[::-1]:
        score *= 5
        score += score_map[char]
    scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])
