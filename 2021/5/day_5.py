from collections import Counter
from dataclasses import dataclass
from typing import Iterator, Tuple


@dataclass
class Coordinate:
    x: int
    y: int

    def __eq__(self, other: object) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self) -> None:
        return f"{self.x}-{self.y}"


def read_lines(filename: str) -> Iterator[str]:
    with open(filename) as f:
        for line in f:
            yield line


def parse_line(line: str) -> Tuple[Coordinate, Coordinate]:
    start, end = line.split(" -> ")
    start_x, start_y = start.split(",")
    end_x, end_y = end.split(",")
    return Coordinate(int(start_x), int(start_y)), Coordinate(int(end_x), int(end_y))


def is_vertical(starting_coordinate: Coordinate, ending_coordinate: Coordinate) -> bool:
    return True if starting_coordinate.x == ending_coordinate.x else False


def is_horizontal(
    starting_coordinate: Coordinate, ending_coordinate: Coordinate
) -> bool:
    return True if starting_coordinate.y == ending_coordinate.y else False


def is_diagonal(starting_coordinate: Coordinate, ending_coordinate: Coordinate) -> bool:
    return abs(starting_coordinate.x - ending_coordinate.x) == abs(
        starting_coordinate.y - ending_coordinate.y
    )


def print_overlapped_coordinates(line_segment_map: Counter) -> None:
    n_overlapped_coordinates = len(
        {
            coordinates
            for coordinates, overlap in line_segment_map.items()
            if overlap > 1
        }
    )
    print(f"There are {n_overlapped_coordinates} overlapped coordinates.")


def add_interm_points(
    start: Coordinate, end: Coordinate, dx: int, dy: int, line_segment_map: Counter
):
    line_segment_map[f"{str(start)}"] += 1
    while not (start == end):
        start.x += dx
        start.y += dy
        line_segment_map[f"{str(start)}"] += 1
    return line_segment_map


def part1(filename: str) -> None:
    print("=" * 10, "Part 1", "=" * 10)
    line_segment_map = Counter()
    lines = read_lines(filename)
    for line in lines:
        start, end = parse_line(line)

        if is_vertical(start, end):
            dy = 1 if start.y < end.y else -1
            line_segment_map = add_interm_points(start, end, 0, dy, line_segment_map)

        elif is_horizontal(start, end):
            dx = 1 if start.x < end.x else -1
            line_segment_map = add_interm_points(start, end, dx, 0, line_segment_map)

    print_overlapped_coordinates(line_segment_map)


def part2(filename: str) -> None:
    print("=" * 10, "Part 2", "=" * 10)
    line_segment_map = Counter()
    lines = read_lines(filename)
    for line in lines:
        start, end = parse_line(line)

        if is_vertical(start, end):
            dy = 1 if start.y < end.y else -1
            line_segment_map = add_interm_points(start, end, 0, dy, line_segment_map)

        elif is_horizontal(start, end):
            dx = 1 if start.x < end.x else -1
            line_segment_map = add_interm_points(start, end, dx, 0, line_segment_map)

        elif is_diagonal(start, end):
            dx = 1 if start.x < end.x else -1
            dy = 1 if start.y < end.y else -1
            line_segment_map = add_interm_points(start, end, dx, dy, line_segment_map)

    print_overlapped_coordinates(line_segment_map)


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
