from collections import defaultdict, Counter


def read_data() -> list[list[str]]:
    with open("input.txt", "r") as f:
        raw = f.read()
        paths = [x.split("-") for x in raw.strip().split("\n")]
        return paths


def create_cave_map(paths: list[list[str]]) -> defaultdict[str, list[str]]:
    mapping = defaultdict(list)
    for path in paths:
        a, b = path
        mapping[a].append(b)
        mapping[b].append(a)
    return mapping


def part1(mapping: defaultdict[str, list[str]]) -> None:
    n_paths = 0

    def bt(cur: list[str]) -> None:
        nonlocal n_paths
        if cur[-1] == "end":
            n_paths += 1
            return
        last_one = cur[-1]
        for n in mapping[last_one]:
            if n not in cur:
                bt(cur + [n])
            elif n.isupper():
                bt(cur + [n])

    bt(["start"])
    print("Part 1", n_paths)


def part2(mapping: defaultdict[str, list[str]]) -> None:
    n_paths = 0

    def bt(cur: list[str]) -> None:
        nonlocal n_paths
        if cur[-1] == "end":
            n_paths += 1
            return
        last_one = cur[-1]
        for n in mapping[last_one]:
            if n not in cur:
                bt(cur + [n])
            elif n.isupper():
                bt(cur + [n])
            elif n in ["start", "end"]:
                continue
            else:
                counter = Counter([x for x in cur if x.islower()])
                if max(counter.values()) == 1:
                    bt(cur + [n])

    bt(["start"])
    print("Part 2", n_paths)


def main() -> None:
    cave_paths = read_data()
    cave_map = create_cave_map(cave_paths)
    part1(cave_map)
    part2(cave_map)


if __name__ == "__main__":
    main()
