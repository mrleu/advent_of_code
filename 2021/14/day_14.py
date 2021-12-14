from typing import Tuple, List
from collections import Counter
import itertools


def read_data() -> List[str]:
    with open("input.txt", "r") as f:
        return f.read().split("\n\n")


def create_polymer_template(
    polymer_template: str,
) -> Tuple[str, Counter[str]]:
    start_char = polymer_template[0]
    cur_template: Counter[str] = Counter()
    for idx in range(len(polymer_template) - 1):
        cur_template[polymer_template[idx : idx + 2]] += 1
    return start_char, cur_template


def create_pair_insertions_map(pair_insertions: str) -> dict[str, str]:
    mapping = dict()
    for x in pair_insertions.strip().split("\n"):
        start, end = x.split(" -> ")
        mapping[start] = end
    return mapping


def difference_between_most_common_and_least_common(
    cur_template: Counter[str], start_char: str
) -> None:
    total_count: Counter[str] = Counter()
    for k, v in cur_template.items():
        total_count[k[1]] += v

    total_count[start_char] += 1
    print("delta", max(total_count.values()) - min(total_count.values()))


def insert_polymer(
    cur_template: Counter[str],
    start_char: str,
    mapping: dict[str, str],
) -> None:
    for i in itertools.count(1):
        for k, count in cur_template.copy().items():
            cur_template[k] -= count
            cur_template[k[0] + mapping[k]] += count
            cur_template[mapping[k] + k[1]] += count
        if i == 10:
            print("=" * 10, "part 1", "=" * 10)
            difference_between_most_common_and_least_common(cur_template, start_char)
        if i == 40:
            print("=" * 10, "part 2", "=" * 10)
            difference_between_most_common_and_least_common(cur_template, start_char)
            break


def main() -> None:
    polymer_template, pair_insertions = read_data()
    start_char, cur_template = create_polymer_template(polymer_template)
    mapping = create_pair_insertions_map(pair_insertions)
    insert_polymer(cur_template, start_char, mapping)


if __name__ == "__main__":
    main()
