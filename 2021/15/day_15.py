import heapq


def read_data():
    with open("input.txt", "r") as f:
        raw = f.read()
        return [list(map(int, list(x))) for x in raw.strip().split("\n")]


def dijkstra(data, multiply):
    nrows = len(data) * multiply
    ncols = len(data[0]) * multiply

    def risk_level(i, j):
        row = len(data)
        col = len(data[0])
        risk = (i // row + j // col + data[i % row][j % col]) % 9
        return 9 if risk == 0 else risk

    distances = {
        (c, r): 0 if (c, r) == (0, 0) else float("inf")
        for r in range(nrows)
        for c in range(ncols)
    }

    heap = [(0, (0, 0))]
    while heap:
        distance, u = heapq.heappop(heap)
        for delta in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            if (neighbor := tuple(map(sum, zip(u, delta)))) in distances:
                if (distance_ := distance + risk_level(*neighbor)) < distances[
                    neighbor
                ]:
                    distances[neighbor] = distance_
                    heapq.heappush(heap, (distance_, neighbor))

    print(distances[(nrows - 1, ncols - 1)])


def main():
    data = read_data()
    print("=" * 10, "part 1", "=" * 10)
    dijkstra(data, multiply=1)

    print("=" * 10, "part 2", "=" * 10)
    dijkstra(data, multiply=5)


if __name__ == "__main__":
    main()
