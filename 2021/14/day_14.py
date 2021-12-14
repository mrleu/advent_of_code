from typing import Tuple, List
from collections import Counter
import itertools


def read_data() -> List[str]:
    with open("input.txt", "r") as f:
        return f.read().split("\n\n")


def create_polymer_template(
    polymer_template: str,
) -> Tuple[str, str, Counter[str]]:
    start_char = polymer_template[0]
    end_char = polymer_template[-1]
    cur_template: Counter[str] = Counter()
    for idx in range(len(polymer_template) - 1):
        cur_template[polymer_template[idx : idx + 2]] += 1
    return start_char, end_char, cur_template


def create_pair_insertions_map(pair_insertions: str) -> dict[str, str]:
    mapping = dict()
    for x in pair_insertions.strip().split("\n"):
        start, end = x.split(" -> ")
        mapping[start] = end
    return mapping


def difference_between_most_common_and_least_common(
    cur_template: Counter[str], start_char: str, end_char: str
) -> None:
    total_count: Counter[str] = Counter()
    for k, v in cur_template.items():
        total_count[k[0]] += v
        total_count[k[1]] += v

    total_count[start_char] += 1
    total_count[end_char] += 1

    print(
        "delta",
        (total_count.most_common()[0][1] // 2)
        - (total_count.most_common()[-1][1] // 2),
    )


def insert_polymer(
    cur_template: Counter[str],
    start_char: str,
    end_char: str,
    mapping: dict[str, str],
) -> None:
    for i in itertools.count(1):
        new_template: Counter[str] = Counter()
        for k, count in cur_template.items():
            new_template[k[0] + mapping[k]] += count
            new_template[mapping[k] + k[1]] += count
        cur_template = new_template
        if i == 10:
            print("=" * 10, "part 1", "=" * 10)
            difference_between_most_common_and_least_common(
                cur_template, start_char, end_char
            )
        if i == 40:
            print("=" * 10, "part 2", "=" * 10)
            difference_between_most_common_and_least_common(
                cur_template, start_char, end_char
            )
            break


def main() -> None:
    polymer_template, pair_insertions = read_data()
    start_char, end_char, cur_template = create_polymer_template(polymer_template)
    mapping = create_pair_insertions_map(pair_insertions)
    insert_polymer(cur_template, start_char, end_char, mapping)


if __name__ == "__main__":
    main()
