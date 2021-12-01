# part 1
files = open('input.txt').read()
clean = files.split('\n')
clean = [float(x) for x in clean if x != '']
N = len(clean)
dp = [0] * N

for i in range(1, len(clean)):
    dp[i] = 1 if clean[i] > clean[i-1] else 0
print(sum(dp))

# part 2 - regular solution
dp = [0] * N
for i in range(3, len(clean)):
    dp[i] = clean[i] + clean[i-1] + clean[i-2]

dp2 = [0] * N
for i in range(3, len(clean)):
    dp2[i] = 1 if dp[i] > dp[i-1] else 0
print(sum(dp2))


# Pandas solution part 1
import pandas as pd
df = pd.read_csv('input.txt', names=['measure'])
df['offset'] = df.shift(1)
df['increased'] = df.apply(lambda x: 1 if x['measure'] > x['offset'] else 0, axis=1)
print(f"Sum is :{df.increased.sum()}")

# Pandas solution part 2
import pandas as pd
df = pd.read_csv('input.txt', names=['measure'])
rolling_df = df.rolling(3).sum()
rolling_df['offset'] = rolling_df.shift(1)
rolling_df['increased'] = rolling_df.apply(lambda x: 1 if x['measure'] > x['offset'] else 0, axis=1)
print(f"Sum is :{rolling_df.increased.sum()}")


# jank pandas
clean = pd.Series(clean).rolling(3).sum().tolist()
N = len(clean)
dp = [0] * N

for i in range(3, len(clean)):
    dp[i] = 1 if clean[i] > clean[i-1] else 0
print(sum(dp))






