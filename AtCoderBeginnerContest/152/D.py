# import sys
# sys.setrecursionlimit(10 ** 6)
def cmb(n, r):
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ABs = {}
    ABs_visited = {}
    for h in range(1, 10):
        for t in range(1, 10):
            ABs.setdefault((h, t), 0)
            ABs_visited.setdefault((h, t), False)

    for n in range(1, N + 1):
        s = str(n)
        h, t = int(s[0]), int(s[-1])
        if not (h == 0 or t == 0):
            ABs[(h, t)] += 1

    ans = 0
    for k in ABs:
        if ABs_visited[k]:
            continue
        h, t = k
        ABs_visited[(h, t)] = True
        # ABs_visited[(t, h)] = True

        # if h == t:
        #     ans += ABs[(h, t)] + cmb(ABs[(h, t)], 2)
        # else:
        #     ans += ABs[(h, t)] * ABs[(t, h)]
        ans += ABs[(h, t)] * ABs[(t, h)]
        # print(k, ABs[k], ans)
        # input()
    # print(ABs)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)
