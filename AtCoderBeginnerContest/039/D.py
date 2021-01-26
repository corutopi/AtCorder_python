# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    S = ['#' * (W + 2)] + ['#' + s + '#' for s in S] + ['#' * (W + 2)]
    bfr = [['.' for _ in range(W + 2)] for _ in range(H + 2)]
    ge = ((h, w) for h in range(1, H + 1) for w in range(1, W + 1))
    for h, w in ge:
        if (S[h - 1][w - 1] == S[h - 1][w] == S[h - 1][w + 1] ==
                S[h][w - 1] == S[h][w] == S[h][w + 1] ==
                S[h + 1][w - 1] == S[h + 1][w] == S[h + 1][w + 1] == '#'):
            bfr[h][w] = '#'
        else:
            bfr[h][w] = '.'

    aft = [['#' for _ in range(W + 2)] for _ in range(H + 2)]
    ge = ((h, w) for h in range(1, H + 1) for w in range(1, W + 1))
    for h, w in ge:
        if bfr[h][w] == '#':
            aft[h][w] = '#'
        else:
            if (bfr[h - 1][w - 1] == bfr[h - 1][w] == bfr[h - 1][w + 1] ==
                    bfr[h][w - 1] == bfr[h][w] == bfr[h][w + 1] ==
                    bfr[h + 1][w - 1] == bfr[h + 1][w] == bfr[h + 1][
                        w + 1] == '.'):
                aft[h][w] = '.'
            else:
                aft[h][w] = '#'
    aft = [''.join(af)for af in aft]
    if all([S[i] == aft[i] for i in range(H + 2)]):
        print('possible')
        [print(''.join(bf[1:-1])) for bf in bfr[1:-1]]
    else:
        print('impossible')


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # H, W = 100, 100
    # S = [random_str(W, '#.') for _ in range(H)]
    # solve(H, W, S)
