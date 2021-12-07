import statistics


def read_file(filename: str) -> list[int]:
    with open(filename) as f:
        return list(map(int, f.read().strip().split(",")))


def part1(cleaned: list[int]) -> None:
    median = round(statistics.median(cleaned))
    minimum_fuel = sum([abs(n - median) for n in cleaned])
    print(f"Minimum fuel is {minimum_fuel}")


def triangular_number(x: int) -> int:
    return ((x ** 2) + x) // 2


def part2(cleaned: list[int]) -> None:
    mean = round(statistics.mean(cleaned))
    closest_to_mean = min(cleaned, key=lambda x: abs(x - mean))

    minimum_fuel = sum([triangular_number(abs(n - closest_to_mean)) for n in cleaned])
    print(f"Minimum fuel is {minimum_fuel}")


def main() -> None:
    cleaned = read_file("input.txt")
    part1(cleaned)
    part2(cleaned)


if __name__ == "__main__":
    main()
