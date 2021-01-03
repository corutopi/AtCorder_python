# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    S = ['#' * (W + 2)] + ['#' + s + '#' for s in S] + ['#' * (W + 2)]
    ans = 0
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if S[h][w] == '#':
                continue
            if S[h + 1][w] == '.':
                ans += 1
            if S[h][w + 1] == '.':
                ans += 1
    print(ans)



if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(H, W, S)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
