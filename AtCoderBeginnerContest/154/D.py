# import sys
# sys.setrecursionlimit(10 ** 6)
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, ps):
    ev = [0] *  (N + 1)       # Expected value
    cs = [0] * (N + 1)        # Cumulative sum
    for i, p in enumerate(ps, 1):
        ev[i] = (p + 1) / 2
        cs[i] = cs[i - 1] + ev[i]

    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, cs[i] - cs[i - K])

    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    ps = [int(i) for i in input().split()]

    # N, K = 200000, 2
    # ps = [i for i in range(1, 200000 + 1)]

    solve(N, K, ps)
