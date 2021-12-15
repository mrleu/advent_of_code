import heapq


def read_data():
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def dijkstra(data, five_times):
    multiple = 5 if five_times else 1
    nrows = len(data) * multiple
    ncols = len(data[0]) * multiple

    def risk_level(i, j):
        row = len(data)
        col = len(data[0])
        risk = (i // row) + (j // col + data[i % row][j % col]) % 9
        return 9 if risk == 0 else risk

    distances = {(c, r): float("inf") for r in range(nrows) for c in range(ncols)}
    start = (0, 0)
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        distance, u = heapq.heappop(heap)
        for delta in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            neighbor = tuple(map(sum, zip(u, delta)))
            if neighbor in distances:
                if (new_dist := distance + risk_level(*neighbor)) < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

    print(distances[(nrows - 1, ncols - 1)])


def main():
    data = read_data()
    print("=" * 10, "part 1", "=" * 10)
    dijkstra(data, five_times=False)

    print("=" * 10, "part 2", "=" * 10)
    dijkstra(data, five_times=True)


if __name__ == "__main__":
    main()
