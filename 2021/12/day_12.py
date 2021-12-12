from collections import defaultdict, Counter


def read_data() -> list[list[str]]:
    with open("input.txt", "r") as f:
        raw = f.read()
        paths = [x.split("-") for x in raw.strip().split("\n")]
        return paths


def create_cave_map(cave_paths: list[list[str]]) -> defaultdict[str, list[str]]:
    cave_map = defaultdict(list)
    for (cave_a, cave_b) in cave_paths:
        cave_map[cave_a].append(cave_b)
        cave_map[cave_b].append(cave_a)
    return cave_map


def part1(cave_map: defaultdict[str, list[str]]) -> None:
    n_paths = 0

    def backtracking(current_path: list[str]) -> None:
        nonlocal n_paths

        if current_path[-1] == "end":
            n_paths += 1
            return

        last_cave = current_path[-1]
        for cave in cave_map[last_cave]:
            if cave not in current_path or cave.isupper():
                backtracking(current_path + [cave])

    backtracking(["start"])
    print("Part 1", n_paths)


def part2(cave_map: defaultdict[str, list[str]]) -> None:
    n_paths = 0

    def backtracking(current_path: list[str]) -> None:
        nonlocal n_paths

        if current_path[-1] == "end":
            n_paths += 1
            return

        last_cave = current_path[-1]
        for cave in cave_map[last_cave]:
            if cave not in current_path or cave.isupper():
                backtracking(current_path + [cave])
            elif cave in ["start", "end"]:
                continue
            else:
                counter = Counter([x for x in current_path if x.islower()])
                if max(counter.values()) == 1:
                    backtracking(current_path + [cave])

    backtracking(["start"])
    print("Part 2", n_paths)


def main() -> None:
    cave_paths = read_data()
    cave_map = create_cave_map(cave_paths)
    part1(cave_map)
    part2(cave_map)


if __name__ == "__main__":
    main()
