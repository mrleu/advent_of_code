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
    dots: set[tuple[int, int]], instructions: list[tuple[str, int]]
) -> set[tuple[int, int]]:
    for idx, (axis, position) in enumerate(instructions):
        temp_dots = set()
        for dot in dots:
            x, y = dot
            check_axis = x if axis == "x" else y
            if check_axis == position:
                continue
            elif check_axis < position:
                temp_dots.add((x, y))
            else:
                temp_dots.add((2 * position - x, y)) if axis == "x" else temp_dots.add(
                    (x, 2 * position - y)
                )

        dots = temp_dots

        if idx == 0:
            read_visible_dots(dots)

    return dots


def read_visible_dots(dots: set[tuple[int, int]]) -> None:
    print("=" * 10, "part 1", "=" * 10)
    print("Number of dots after first fold:", len(dots))


def create_transparent_paper(dots: set[tuple[int, int]]) -> list[list[str]]:
    max_x = max([x for (x, y) in dots])
    max_y = max([y for (x, y) in dots])
    transparent_paper = []
    for i in range(max_y + 1):
        transparent_paper.append(["." for _ in range(max_x + 1)])
    for (x, y) in dots:
        transparent_paper[y][x] = "#"
    return transparent_paper


def read_transparent_paper(transparent_paper: list[list[str]]) -> None:
    print("=" * 10, "part 2", "=" * 10)
    for row in transparent_paper:
        print("".join(row))


def main() -> None:
    dots, instructions = read_data()
    dots = fold_paper(dots, instructions)
    transparent_paper = create_transparent_paper(dots)
    read_transparent_paper(transparent_paper)


if __name__ == "__main__":
    main()
