# 解説を参考に作成

# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import math
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, As):
    ans = max(As)
    l, r = 1, ans
    for _ in range(30):
        m = (l + r) // 2
        cnt = 0
        for A in As:
            cnt += math.ceil(A / m) - 1
        if cnt <= K:
            ans = min(ans, m)
            r = m - 1
        else:
            l = m + 1
        if l > r:
            break
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, K, As)
