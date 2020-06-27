# 解説を参考に作成


# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ans = 0
    for i in range(1, N + 1):
        ans += (i + i * (N // i)) * (N // i) // 2
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)
