with open("input.txt", "r") as f:
    raw = f.read().strip()

corrupted = []
incompletes = []
close_open_map = {"}": "{", ")": "(", ">": "<", "]": "["}
open_close_map = {v: k for k, v in close_open_map.items()}
corrupted_character_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_character_points = {")": 1, "]": 2, "}": 3, ">": 4}

for line in raw.split("\n"):
    queue = []
    broken = False
    for char in line:
        if char in open_close_map.keys():
            queue.append(char)
        else:
            take_out = queue.pop()
            if take_out != close_open_map[char]:
                corrupted.append(char)
                broken = True
    if not broken:
        incompletes.append(list(reversed([open_close_map[x] for x in queue])))

print("Part 1 score:", sum([corrupted_character_points[char] for char in corrupted]))

scores = []
for incomplete in incompletes:
    score = 0
    for char in incomplete:
        score *= 5
        score += incomplete_character_points[char]
    scores.append(score)
sorted_scores = sorted(scores)
print("Part 2 score:", sorted_scores[int((len(scores) - 1) / 2)])
