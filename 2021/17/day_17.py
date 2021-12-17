from dataclasses import dataclass
import re


def parse_data(data_input):
    parsed = list(map(int, re.findall(r"[-]?\d+", data_input)))
    return (parsed[0], parsed[1]), (parsed[2], parsed[3])


def in_box(coordinate, target_area):
    target_x, target_y = target_area
    if (
        target_x[0] <= coordinate.x <= target_x[1]
        and target_y[0] <= coordinate.y <= target_y[1]
    ):
        return True
    return False


@dataclass
class Coordinate:
    x: int
    y: int


def trickshot(x_grad, y_grad, target_area):
    furthest = target_area[1][0]
    coordinate = Coordinate(0, 0)
    ys = []
    while coordinate.y >= furthest:
        coordinate.x += x_grad
        coordinate.y += y_grad

        ys.append(coordinate.y)
        if in_box(coordinate, target_area):
            return True, max(ys)

        if x_grad < 0:
            x_grad += 1
        elif x_grad == 0:
            x_grad = 0
        elif x_grad > 0:
            x_grad -= 1

        y_grad -= 1

        if coordinate.y < furthest:
            return False, None


def grid_search(target_area):
    works = set()
    highest = []
    for x_grad in range(-200, 200):
        for y_grad in range(-200, 200):
            made_it, high_y = trickshot(x_grad, y_grad, target_area)
            if made_it:
                works.add((x_grad, y_grad))
                highest.append(high_y)
    print("Highest position:", max(highest))
    print("Unique velocity", len(works))


def main():
    data_input = "target area: x=56..76, y=-162..-134"
    target_area = parse_data(data_input)
    grid_search(target_area)


if __name__ == "__main__":
    main()
