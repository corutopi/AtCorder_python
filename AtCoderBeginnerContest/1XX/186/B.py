# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, A):
    min_brock = inf
    for ah in A:
        min_brock = min(min_brock, min(ah))
    ans = 0
    for h in range(H):
        for w in range(W):
            ans += A[h][w] - min_brock
    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
