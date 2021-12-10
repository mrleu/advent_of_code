with open("input.txt", "r") as f:
    raw = f.read().strip()

corrupted = []
incompletes = []
mapping = {"}": "{", ")": "(", ">": "<", "]": "["}
rev_map = {v: k for k, v in mapping.items()}
points_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
open_map = {")": 1, "]": 2, "}": 3, ">": 4}

for line in raw.split("\n"):
    queue = []
    broken = False
    for char in line:
        if char in ["[", "(", "<", "{"]:
            queue.append(char)
        else:
            take_out = queue.pop()
            if take_out != mapping[char]:
                corrupted.append(char)
                broken = True
    if not broken:
        incompletes.append(list(reversed([rev_map[x] for x in queue])))

print("Part 1 score:", sum([points_map[char] for char in corrupted]))
scores = []
for incomplete in incompletes:
    n = 0
    for char in incomplete:
        n *= 5
        n += open_map[char]
    scores.append(n)

sorted_scores = sorted(scores)
print("Part 2 score:", sorted_scores[int((len(scores) - 1) / 2)])
