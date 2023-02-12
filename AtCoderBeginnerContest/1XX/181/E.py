# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect

# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, H, W):
    H.sort()
    # make list of pair right
    pair_right = [abs(H[i] - H[i + 1]) for i in
                  range(0, N - 1, 2)]  # remove last
    pair_right_sum = [0]
    for pr in pair_right:
        pair_right_sum.append(pair_right_sum[-1] + pr)
    # make list of pair left
    pair_left = [abs(H[i] - H[i + 1]) for i in range(1, N, 2)]  # remove first
    pair_left_sum = [0]
    for pl in pair_left:
        pair_left_sum.append(pair_left_sum[-1] + pl)
    # make pair W and nealy child, and other nealy pairs.
    ans = inf
    for w in W:
        ins = bisect.bisect_right(H, w)
        w_pair = ins if ins % 2 == 0 else ins - 1
        tmp_ans = abs(w - H[w_pair]) + \
                  pair_right_sum[ins // 2] + \
                  pair_left_sum[-1] - pair_left_sum[ins // 2]
        ans = min(ans, tmp_ans)
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    H = [int(i) for i in input().split()]
    W = [int(i) for i in input().split()]
    solve(N, M, H, W)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N, M = 2 * 10 ** 5 - 1, 2 * 10 ** 5
    # H = [randint(1, 10 ** 9) for _ in range(N)]
    # W = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, M, H, W)
