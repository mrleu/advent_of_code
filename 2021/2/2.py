raw = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# part 1
files = open('input.txt').read().split('\n')[:~0]
parsed = [x.split(' ') for x in files]
start = [0, 0]
for (d, idx) in parsed:
    idx = int(idx)
    if d == 'forward':
        start[0] += idx
    elif d == 'down':
        start[1] += idx
    elif d == 'up':
        start[1] -= idx
print(f"Solution for part 1: {start[0] * start[1]}")

# part 2
start = [0, 0, 0]
for (d, idx) in parsed:
    idx = int(idx)
    if d == 'forward':
        start[0] += idx
        start[1] += (start[2] * idx)
    elif d == 'down':
        start[2] += idx
    elif d == 'up':
        start[2] -= idx
print(f"Solution for part 2: {start[0] * start[1]}")

# pandas part 1
import pandas as pd
df = pd.read_csv('input.txt', names=['direction', 'steps'], sep=' ')
df['steps'] = df.apply(lambda x: -x['steps'] if x['direction'] =='up' else x['steps'], axis=1)
solution = df[df.direction =='forward'].steps.sum()  * df[~(df.direction == 'forward')].steps.sum()
print(f"Solution for part 1 in pandas: {solution}")

# pandas part 2
import pandas as pd
from functools import reduce
import operator
df = pd.read_csv('input.txt', names=['direction', 'size'], sep=' ')
mapping_dict = {'down':1,'up':-1}
df['sign'] = df['direction'].map(mapping_dict)
df['aim'] = (df['size'] * df['sign']).fillna(0)
df['aim_sum'] = df['aim'].cumsum()
df['depth'] = df['aim_sum'] * df['size']
out = df.query('direction == "forward"')[['size','depth']].sum()
solution = reduce(operator.mul, out.tolist())
print(f"Solution for part 2 in pandas: {solution}")
