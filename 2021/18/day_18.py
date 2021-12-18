import math


def convert(ln):
    return [int(s) if s.isdigit() else s for s in ln.rstrip()]


def add(base, datum):
    if not base:
        return datum
    return ["["] + base + [","] + datum + ["]"]


def isdigit(k):
    return isinstance(k, int)


def magnitude(datum):
    while len(datum) > 1:
        for i in range(len(datum)):
            if isdigit(datum[i]) and isdigit(datum[i + 2]):
                datum = (
                    datum[: i - 1] + [datum[i] * 3 + datum[i + 2] * 2] + datum[i + 4 :]
                )
                break
    return datum[0]


def explode(datum, idx):
    left = datum[idx + 1]
    right = datum[idx + 3]
    for new_idx in range(idx - 1, -1, -1):
        if isdigit(datum[new_idx]):
            datum[new_idx] += left
            break
    for new_idx in range(idx + 5, len(datum)):
        if isdigit(datum[new_idx]):
            datum[new_idx] += right
            break
    return datum[:idx] + [0] + datum[idx + 5 :]


def split(datum, idx):
    halved = datum[idx] / 2
    return (
        datum[:idx]
        + ["[", math.floor(halved), ",", math.ceil(halved), "]"]
        + datum[idx + 1 :]
    )


def update(datum):
    changed = True
    while changed:
        changed = False
        depth = 0
        for idx, char in enumerate(datum):
            if char == "]":
                depth -= 1
            elif char == "[":
                depth += 1
                if depth == 5:
                    datum = explode(datum, idx)
                    changed = True
                    break
        if changed:
            continue
        for idx, char in enumerate(datum):
            if isdigit(char) and char >= 10:
                datum = split(datum, idx)
                changed = True
                break
    return datum


def part1(data):
    base = []
    for datum in data:
        base = add(base, datum)
        base = update(base)
    return magnitude(base)


def part2(data):
    max_val = 0
    for datum in data:
        for datum2 in data:
            if datum == datum2:
                continue
            val = magnitude(update(add(datum, datum2)))
            max_val = max(max_val, val)
    return max_val


raw = open("input.txt", "r").read()
data = [convert(d) for d in raw.splitlines()]
print(part1(data))
print(part2(data))
