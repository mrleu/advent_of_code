from collections import Counter
from dataclasses import dataclass
from typing import Iterator, Tuple


@dataclass
class Coordinate:
    x: int
    y: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"{self.x}-{self.y}"


class LineSegmentMap:
    def __init__(self) -> None:
        self.counter: Counter[str] = Counter()

    def add_interm_points(
        self, start: Coordinate, end: Coordinate, dx: int, dy: int
    ) -> None:
        self.counter[str(start)] += 1
        while not (start == end):
            start.x += dx
            start.y += dy
            self.counter[str(start)] += 1

    def print_overlapped_coordinates(self) -> None:
        n_overlapped_coordinates = len(
            {
                coordinates
                for coordinates, overlap in self.counter.items()
                if overlap > 1
            }
        )
        print(f"There are {n_overlapped_coordinates} overlapped coordinates.")


def read_lines(filename: str) -> Iterator[str]:
    with open(filename) as f:
        yield from f


def parse_line(line: str) -> Tuple[Coordinate, Coordinate]:
    start, end = line.split(" -> ")
    start_x, start_y = map(int, start.split(","))
    end_x, end_y = map(int, end.split(","))
    return (Coordinate(start_x, start_y), Coordinate(end_x, end_y))


def is_vertical(start: Coordinate, end: Coordinate) -> bool:
    return True if start.x == end.x else False


def is_horizontal(start: Coordinate, end: Coordinate) -> bool:
    return True if start.y == end.y else False


def is_diagonal(start: Coordinate, end: Coordinate) -> bool:
    return abs(start.x - end.x) == abs(start.y - end.y)


def part1(filename: str) -> None:
    print("=" * 10, "Part 1", "=" * 10)
    line_segment_map = LineSegmentMap()
    lines = read_lines(filename)
    for line in lines:
        start, end = parse_line(line)

        if is_vertical(start, end):
            dx, dy = 0, 1 if start.y < end.y else -1

        elif is_horizontal(start, end):
            dx, dy = 1 if start.x < end.x else -1, 0

        else:
            continue

        line_segment_map.add_interm_points(start, end, dx, dy)
    line_segment_map.print_overlapped_coordinates()


def part2(filename: str) -> None:
    print("=" * 10, "Part 2", "=" * 10)
    line_segment_map = LineSegmentMap()
    lines = read_lines(filename)
    for line in lines:
        start, end = parse_line(line)

        if is_vertical(start, end):
            dx, dy = 0, 1 if start.y < end.y else -1

        elif is_horizontal(start, end):
            dx, dy = 1 if start.x < end.x else -1, 0

        elif is_diagonal(start, end):
            dx = 1 if start.x < end.x else -1
            dy = 1 if start.y < end.y else -1

        else:
            continue

        line_segment_map.add_interm_points(start, end, dx, dy)
    line_segment_map.print_overlapped_coordinates()


if __name__ == "__main__":
    print("Starting day 5")
    part1("input.txt")
    part2("input.txt")
