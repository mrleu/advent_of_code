from collections import Counter
from typing import Tuple, Iterable


def read_lines(filename: str) -> Iterable[Tuple[(list[str], list[frozenset[str]])]]:
    with open(filename, "r") as f:
        for line in f.readlines():
            segment_display, four_digits = line.split(" | ")
            yield segment_display.strip().split(" "), [
                frozenset(codes) for codes in four_digits.strip().split(" ")
            ]


def part1(filename: str) -> None:
    print("=" * 10, "Part 1", "=" * 10)
    easy_map = {"1": 2, "4": 4, "7": 3, "8": 7}
    count = 0
    for _, four_digits in read_lines(filename):
        for digit in four_digits:
            if len(digit) in easy_map.values():
                count += 1
    print(f"Total times the numbers appeard: {count}")


def part2(filename: str) -> None:
    print("=" * 10, "Part 2", "=" * 10)
    total_n = []
    for segment_display, four_digits in read_lines(filename):
        digit_mapping = decode_digits(segment_display)
        decoded_four_digits = compute_digits(four_digits, digit_mapping)
        total_n.append(decoded_four_digits)
    print("Total sum of the decoded digits:", sum(total_n))


def decode_digits(segment_display: list[str]) -> dict[str, frozenset[str]]:
    result = {}
    for d in segment_display:
        if len(d) == 2:
            result["1"] = frozenset(d)
        elif len(d) == 3:
            result["7"] = frozenset(d)
        elif len(d) == 4:
            result["4"] = frozenset(d)
        elif len(d) == 7:
            result["8"] = frozenset(d)
    # find 3
    result["3"] = [
        frozenset(x)
        for x in segment_display
        if len(x) == 5 and result["1"].issubset(set(x))
    ][0]

    # find bottom left
    bottom_left = Counter(
        [y for x in segment_display if len(x) > 3 for y in x]
    ).most_common()[-1][0]
    result["9"] = frozenset(
        [
            x
            for x in segment_display
            if len(x) == 6 and not set(bottom_left).issubset(set(x))
        ][0]
    )
    result["2"] = frozenset(
        [
            x
            for x in segment_display
            if len(x) == 5 and set(bottom_left).issubset(set(x))
        ][0]
    )
    result["5"] = frozenset(
        [x for x in segment_display if len(x) == 5 and set(x) not in result.values()][0]
    )
    result["0"] = frozenset(
        [
            x
            for x in segment_display
            if len(x) == 6
            and set(x) not in result.values()
            and result["1"].issubset(set(x))
        ][0]
    )
    result["6"] = frozenset(
        [x for x in segment_display if len(x) == 6 and set(x) not in result.values()][0]
    )
    return result


def compute_digits(
    raw_digit: list[frozenset[str]], digit_mapping: dict[str, frozenset[str]]
) -> int:
    digit_result = []
    for raw in raw_digit:
        digit = [k for k, v in digit_mapping.items() if v == raw][0]
        digit_result.append(digit)
    return int("".join(digit_result))


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
