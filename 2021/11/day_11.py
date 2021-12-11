import itertools

N_FLASHES = 0
COVERED = 100


def read_data() -> list[list[int]]:
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def flash(matrix: list[list[int]], row: int, col: int) -> None:
    global N_FLASHES
    N_FLASHES += 1
    matrix[row][col] = COVERED
    for new_row, new_col in [
        (row + dy, col + dx) for dy, dx in itertools.product([0, 1, -1], repeat=2)
    ]:
        if (
            0 <= new_row < len(matrix)
            and 0 <= new_col < len(matrix[0])
            and matrix[new_row][new_col] != COVERED
        ):
            matrix[new_row][new_col] += 1

    ready_to_flash(matrix)
    matrix[row][col] = 0


def increase_energy(matrix: list[list[int]]) -> None:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] += 1


def ready_to_flash(matrix: list[list[int]]) -> None:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != COVERED and matrix[row][col] > 9:
                flash(matrix, row, col)


def main() -> None:
    matrix = read_data()
    for n in itertools.count(1):
        increase_energy(matrix)
        ready_to_flash(matrix)

        if n == 100:
            print("Part 1: Number of flashes", N_FLASHES)

        if sum([energy for row in matrix for energy in row]) == 0:
            print("Part 2: Hit zero at", n)
            break


if __name__ == "__main__":
    main()
