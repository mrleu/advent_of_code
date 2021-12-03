raw = """00100
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


data = raw.split("\n")

data = open("input.txt").read().splitlines()
dp = [0] * len(data[0])
total_n = len(data)

for row_n, row in enumerate(data):
    for col in range(len(row)):
        dp[col] += int(data[row_n][col])

result = "".join(["1" if x > (total_n // 2) else "0" for x in dp])
decimal_gamma = int(result, 2)
decimal_epsilon = int("".join(["0" if x == "1" else "1" for x in result]), 2)
print(f"Part 1 result is {decimal_gamma * decimal_epsilon}")

# part 2
data = open("input.txt").read().splitlines()
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
print(f"Part 2 result is {int(oxygen,2) * int(carbon, 2)}")
