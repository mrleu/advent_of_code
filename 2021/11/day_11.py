n_flashes = 0
COVERED = 100


def read_data() -> list[list[int]]:
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def flash(matrix: list[list[int]], row: int, col: int) -> list[list[int]]:
    global n_flashes
    n_flashes += 1
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, -1), (-1, 0)]
    matrix[row][col] = COVERED
    for dy, dx in directions:
        new_row = row + dy
        new_col = col + dx
        if (
            0 <= new_row < len(matrix)
            and 0 <= new_col < len(matrix[0])
            and matrix[new_row][new_col] != COVERED
        ):
            matrix[new_row][new_col] += 1

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != COVERED and matrix[r][c] > 9:
                flash(matrix, r, c)
    matrix[row][col] = 0
    return matrix


def main() -> None:
    matrix = read_data()
    for n in range(300):

        # increase everything by one
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += 1

        # flash
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] > 9:
                    flash(matrix, row, col)

        if n + 1 == 100:
            print("Part 1: Number of flashes", n_flashes)
        if all([set(row) == {0} for row in matrix]):
            print("Part 2: Hit zero at", n + 1)
            break


if __name__ == "__main__":
    main()
