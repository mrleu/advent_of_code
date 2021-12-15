import copy
import heapq


def read_data():
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def five_times(data):
    prev_updated = []
    for row in data:
        temp = row.copy()
        for n in range(1, 5):
            temp += [x + n if x + n <= 9 else x + n - 9 for x in row]
        prev_updated.append(temp)

    updated = []
    updated += copy.deepcopy(prev_updated)
    for n in range(1, 5):
        new_temp = copy.deepcopy(prev_updated)
        for row in range(len(new_temp)):
            for col in range(len(new_temp[0])):
                new_temp[row][col] = (
                    new_temp[row][col] + n
                    if new_temp[row][col] + n <= 9
                    else new_temp[row][col] + n - 9
                )
        updated += new_temp
    return updated


def find_mininum_path(data):
    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    seen = dict()

    while True:
        risk_level, current = heapq.heappop(heap)

        if current[0] == len(data[0]) - 1 and current[1] == len(data) - 1:
            print(risk_level)
            break

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nei_x, nei_y = current[0] + dx, current[1] + dy
            if 0 <= nei_x < len(data[0]) and 0 <= nei_y < len(data):
                new_cost = risk_level + data[nei_y][nei_x]

                if (nei_x, nei_y) in seen and seen[(nei_x, nei_y)] <= new_cost:
                    continue

                seen[(nei_x, nei_y)] = new_cost
                heapq.heappush(heap, (new_cost, (nei_x, nei_y)))


def main():
    data = read_data()
    print("=" * 10, "part 1", "=" * 10)
    find_mininum_path(data)
    five_times_data = five_times(data)
    print("=" * 10, "part 2", "=" * 10)
    find_mininum_path(five_times_data)


if __name__ == "__main__":
    main()
