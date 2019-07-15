N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 10 ** 9 + 7

I = [[j for j in range(N) if Ai[j]] for Ai in A]

memo = [-1] * (1 << N)
memo[0] = 1

# print(I)
def dfs(S, c):
    # print('args', S, c)
    if memo[S] != -1:
        return memo[S]

    r = 0
    for i in I[c]:  # bit count
        # print(S & (1 << i))
        if S & (1 << i):
            r += dfs(S ^ (1 << i), c + 1)
    memo[S] = r = r % MOD
    return r


# print('length', len(memo))
print(dfs((1 << N) - 1, 0))
# print(memo)
