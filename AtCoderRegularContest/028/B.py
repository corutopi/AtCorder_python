# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect

# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, X):
    age_list = []
    for i in range(N):
        idx = bisect.bisect_right(age_list, [X[i], i + 1])
        if idx == len(age_list):
            age_list.append([X[i], i + 1])
        else:
            age_list.insert(idx, [X[i], i + 1])
        if len(age_list) >= K:
            print(age_list[K - 1][1])


if __name__ == '__main__':
    N, K = map(int, input().split())
    X = [int(i) for i in input().split()]
    solve(N, K, X)

    # # test
    # import random
    # from random import randint
    # from func import random_str, random_ints
    # N, K = 10 ** 5, randint(1, 10 ** 5)
    # X = [i for i in range(1, N + 1)]
    # random.sample(X, N)
    # solve(N, K, X)
