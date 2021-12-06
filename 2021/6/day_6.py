"""
Day 6 of Advent of Code.
"""
from collections import Counter

NEW_FISH_TIMER = 8
EXISTING_FISH_TIMER = 6


def read_lanternfish(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().strip().split(",")


def count_lanternfish(filename: str, days: int) -> None:
    lanternfish = Counter(map(int, read_lanternfish(filename)))
    for _ in range(days):
        respawn_fish = lanternfish.pop(0, 0)
        lanternfish = Counter(
            {timer - 1: count for timer, count in lanternfish.items()}
        ) + Counter({EXISTING_FISH_TIMER: respawn_fish, NEW_FISH_TIMER: respawn_fish})
    n_lanternfish = sum(lanternfish.values())
    print(f"Total Number of lanternfish: {n_lanternfish}")


def part1(filename: str) -> None:
    print("Part 1")
    count_lanternfish(filename=filename, days=80)


def part2(filename: str) -> None:
    print("Part 2")
    count_lanternfish(filename=filename, days=256)


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
