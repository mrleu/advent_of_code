raw = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """

# preprocessing
raw = open("input.txt").read()
numbers, *boards = raw.strip().split("\n\n")
for idx in range(len(boards)):
    boards[idx] = [
        [y for y in x.split(" ") if y != ""] for x in boards[idx].split("\n")
    ]
numbers = numbers.split(",")


def win(board):
    for row in range(len(board)):
        if set(board[row]) == set("#"):
            return True
    for col in range(len(board[0])):
        if set([board[i][col] for i in range(len(board[0]))]) == set("#"):
            return True
    return False


won = False
winning_number = None
won_idx = None

for num_idx, number in enumerate(numbers):
    if not won:
        for idx, board in enumerate(boards):
            for row in range(5):
                for col in range(5):
                    if number == board[row][col]:
                        board[row][col] = "#"

            if win(board):
                won = True
                winning_number = int(number)
                won_idx = idx

remain_sum = sum([int(col) for row in boards[won_idx] for col in row if col != "#"])
print(f" part 1: remain sum is {remain_sum}, total is {remain_sum*winning_number}")


# part 2
raw = open("input.txt").read()
numbers, *boards = raw.strip().split("\n\n")

for idx in range(len(boards)):
    boards[idx] = [
        [y for y in x.split(" ") if y != ""] for x in boards[idx].split("\n")
    ]

numbers = numbers.split(",")
last_one = None
won = set()

for num_idx, number in enumerate(numbers):
    for idx, board in enumerate(boards):
        for row in range(5):
            for col in range(5):
                if number == board[row][col] and idx not in won:
                    board[row][col] = "#"

                if win(board) and idx not in won:
                    won.add(idx)
                    last_one = (num_idx, idx, number)

won_idx = last_one[1]
winning_number = int(last_one[2])
remain_sum = sum([int(col) for row in boards[won_idx] for col in row if col != "#"])
print(
    f"part 2: won indx: {won_idx}, winning_number: {winning_number}, remain sum is {remain_sum}, total is {remain_sum*winning_number}"
)
