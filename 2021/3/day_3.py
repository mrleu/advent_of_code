"""
Day 3 of advent of code.
"""

RAW = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


data = RAW.split("\n")

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

dp = [0] * len(data[0])
total_n = len(data)

for row_n, row in enumerate(data):
    for col in range(len(row)):
        dp[col] += int(data[row_n][col])

RESULT = "".join(["1" if x > (total_n // 2) else "0" for x in dp])
DECIMAL_GAMMA = int(RESULT, 2)
DECIMAL_EPSILON = int("".join(["0" if x == "1" else "1" for x in RESULT]), 2)
print(f"Part 1 RESULT is {DECIMAL_GAMMA * DECIMAL_EPSILON}")

# part 2
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()
total_n = len(data[0])

queue = data
for i in range(total_n):
    if len(queue) > 1:
        zero_queue = [d for d in queue if d[i] == "0"]
        one_queue = [d for d in queue if d[i] == "1"]
        queue = one_queue if len(one_queue) >= len(zero_queue) else zero_queue
oxygen = queue[0]

queue = data
for i in range(total_n):
    if len(queue) > 1:
        zero_queue = [d for d in queue if d[i] == "0"]
        one_queue = [d for d in queue if d[i] == "1"]
        queue = one_queue if len(one_queue) < len(zero_queue) else zero_queue
carbon = queue[0]
print(f"Oxygen is {oxygen}, carbon is {carbon}")
print(f"Part 2 RESULT is {int(oxygen,2) * int(carbon, 2)}")
