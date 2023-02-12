# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, a, k, b):
    x = a
    bird = [x]
    read = [0] * (N + 1)
    read[x] = 1
    while read[b[x - 1]] == 0:
        x = b[x - 1]
        bird.append(x)
        read[x] = 1
    loop_start = 0
    for i in range(len(bird)):
        if bird[i] == b[x - 1]:
            loop_start = i
            break
    in_loop = bird[loop_start:]
    if k < len(bird):
        print(bird[k])
    else:
        print(in_loop[(k - loop_start) % len(in_loop)])


if __name__ == '__main__':
    N, a = map(int, input().split())
    k = int(input())
    b = [int(i) for i in input().split()]
    solve(N, a, k, b)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 10 ** 5
    # a = randint(1, N)
    # k = randint(10 ** 99999, 10 ** 100000)
    # b = random_ints(N, 1, N)
    # solve(N, a, k, b)
