import heapq
from operator import mul
from dataclasses import dataclass
from functools import reduce


DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
FILLED = 100


@dataclass
class Point:
    num: int
    row_idx: int
    col_idx: int


def read_data() -> list[list[int]]:
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def get_low_points(data: list[list[int]]) -> list[Point]:
    low_points = []
    rows = len(data)
    cols = len(data[0])

    for i in range(rows):
        for j in range(cols):
            lowest = True
            for di, dj in DIRECTIONS:
                nei_i = i + di
                nei_j = j + dj
                if 0 <= nei_i < rows and 0 <= nei_j < cols:
                    if data[nei_i][nei_j] <= data[i][j]:
                        lowest = False
            if lowest:
                low_points.append(Point(data[i][j], i, j))
    return low_points


def get_total_sizes(low_points: list[Point], data: list[list[int]]) -> list[int]:
    rows = len(data)
    cols = len(data[0])

    total_sizes = []
    for low_point in low_points:
        data[low_point.row_idx][low_point.col_idx] = FILLED
        queue = [(low_point.row_idx, low_point.col_idx)]
        size_count = 1
        while queue:
            point = queue.pop()
            i, j = point
            for di, dj in DIRECTIONS:
                nei_i = i + di
                nei_j = j + dj
                if (
                    0 <= nei_i < rows
                    and 0 <= nei_j < cols
                    and data[nei_i][nei_j] not in [9, FILLED]
                ):
                    size_count += 1
                    data[nei_i][nei_j] = FILLED
                    queue.append((nei_i, nei_j))
        total_sizes.append(size_count)
    return total_sizes


def part1(low_points: list[Point]) -> None:
    print("Sum of low points are:", sum([p.num + 1 for p in low_points]))


def part2(low_points: list[Point], data: list[list[int]]) -> None:
    total_sizes = get_total_sizes(low_points, data)
    product_three_largest = reduce(mul, heapq.nlargest(3, total_sizes))
    print(f"Three Largest basin product is:", product_three_largest)


def main() -> None:
    data = read_data()
    low_points = get_low_points(data)
    part1(low_points)
    part2(low_points, data)


if __name__ == "__main__":
    main()
