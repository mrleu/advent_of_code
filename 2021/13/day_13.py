def read_data() -> tuple[set[tuple[int, int]], list[tuple[str, int]]]:
    with open("input.txt", "r") as f:
        raw = f.read().strip()
        raw_dots, raw_instructions = raw.split("\n\n")

        dots = set()
        for dot in raw_dots.split("\n"):
            x, y = dot.split(",")
            dots.add((int(x), int(y)))

        instructions = []
        for instruction in raw_instructions.replace("fold along ", "").split("\n"):
            axis, position = instruction.split("=")
            instructions.append((axis, int(position)))

        return dots, instructions


def fold_paper(
    dots: set[tuple[int, int]],
    instructions: list[tuple[str, int]],
    one_fold: bool = False,
) -> set[tuple[int, int]]:
    for (axis, position) in instructions:
        new_dots = set()
        for dot in dots:
            x, y = dot
            if axis == "y":
                if y < position:
                    new_dots.add((x, y))
                elif y == position:
                    continue
                else:
                    new_dots.add((x, position - (y - position)))
            if axis == "x":
                if x < position:
                    new_dots.add((x, y))
                elif x == position:
                    continue
                else:
                    new_dots.add((position - (x - position), y))
        dots = new_dots
        if one_fold:
            break
    return dots


def create_transparent_paper(dots: set[tuple[int, int]]) -> list[list[str]]:
    max_x = max([x for (x, y) in dots])
    max_y = max([y for (x, y) in dots])
    grid = []
    for i in range(max_y + 1):
        grid.append(["." for _ in range(max_x + 1)])
    for (x, y) in dots:
        grid[y][x] = "#"
    return grid


def read_transparent_paper(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))


def part1(dots: set[tuple[int, int]], instructions: list[tuple[str, int]]) -> None:
    print("=" * 10, "part 1", "=" * 10)
    dots = fold_paper(dots, instructions, one_fold=True)
    print("Number of dots after first fold:", len(dots))


def part2(dots: set[tuple[int, int]], instructions: list[tuple[str, int]]) -> None:
    print("=" * 10, "part 2", "=" * 10)
    dots = fold_paper(dots, instructions, one_fold=False)
    grid = create_transparent_paper(dots)
    read_transparent_paper(grid)


def main() -> None:
    dots, instructions = read_data()
    part1(dots, instructions)
    part2(dots, instructions)


if __name__ == "__main__":
    main()
