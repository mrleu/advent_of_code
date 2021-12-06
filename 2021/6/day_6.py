"""
Day 6 of Advent of Code.
"""
from collections import Counter


def read_lanternfish(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().strip().split(",")


def count_lanternfish(filename: str, days: int) -> None:
    lanternfish = Counter(map(int, read_lanternfish(filename)))
    for _ in range(days):
        respawn_fish = lanternfish.pop(0, 0)
        lanternfish = Counter(
            {timer - 1: count for timer, count in lanternfish.items()}
        ) + Counter({6: respawn_fish, 8: respawn_fish})
    n_lanternfish = sum(lanternfish.values())
    print(f"Total Number of lanternfish: {n_lanternfish}")


def part1(filename: str) -> None:
    count_lanternfish(filename, 80)


def part2(filename: str) -> None:
    count_lanternfish(filename, 256)


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
