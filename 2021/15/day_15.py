import heapq


def read_data():
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def five_times(data):
    n_row = len(data)
    n_col = len(data[0])

    for row in data:
        for chunk in range(4):
            row += [((col + 1) % 10) or 1 for col in row[n_col * chunk :]]

    for chunk in range(4):
        for row in data[n_row * chunk :]:
            data.append([((col + 1) % 10) or 1 for col in row])
    return data


def dijkstra(data, unvisited_set={}, nodes={}):
    distances = {
        (c, r): float("inf") for r in range(len(data)) for c in range(len(data[0]))
    }
    start = (0, 0)
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        distance, u = heapq.heappop(heap)
        for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nr, nc = u[0] + dr, u[1] + dc
            if 0 <= nr < len(data) and 0 <= nc < len(data[0]):
                neighbor = (nr, nc)
                if (new_dist := distance + data[nr][nc]) < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
    print(distances[(len(data[0]) - 1, len(data) - 1)])


def main():
    data = read_data()
    print("=" * 10, "part 1", "=" * 10)
    dijkstra(data)

    five_times_data = five_times(data)
    print("=" * 10, "part 2", "=" * 10)
    dijkstra(five_times_data)


if __name__ == "__main__":
    main()
