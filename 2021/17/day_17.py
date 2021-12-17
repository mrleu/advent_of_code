import re


def parse_data(data_input):
    parsed = list(map(int, re.findall(r"[-]?\d+", data_input)))
    return (parsed[0], parsed[1]), (parsed[2], parsed[3])


def in_box(coordinate, target_area):
    target_x, target_y = target_area
    if (
        target_x[0] <= coordinate[0] <= target_x[1]
        and target_y[0] <= coordinate[1] <= target_y[1]
    ):
        return True
    return False


def trickshot(x, y, target_area):
    furthest = target_area[1][0]
    coordinate = [0, 0]
    ys = []
    while coordinate[1] >= furthest:
        # print("x, y", x, y, "coordinate", coordinate)
        coordinate[0] += x
        coordinate[1] += y
        ys.append(coordinate[1])
        if in_box(coordinate, target_area):
            # print(f"Hit in the coordinate! at {coordinate}, with highest y at {max(ys)}")
            return (True, max(ys))
            break
        if x < 0:
            x += 1
        elif x == 0:
            x = 0
        elif x > 0:
            x -= 1
        y -= 1
        if coordinate[1] < furthest:
            # print("sorry, didn't hit")
            return (False, None)


def grid_search(target_area):
    works = set()
    highest = []
    for x in range(-200, 200):
        for y in range(-200, 200):
            made_it, high_y = trickshot(x, y, target_area)
            if made_it:
                # print("Velocity that works:", (x, y))
                works.add((x, y))
                highest.append(high_y)
    print("Highest position:", max(highest))
    print("Unique velocity", len(works))


def main():
    data_input = "target area: x=56..76, y=-162..-134"
    target_area = parse_data(data_input)
    grid_search(target_area)


if __name__ == "__main__":
    main()
