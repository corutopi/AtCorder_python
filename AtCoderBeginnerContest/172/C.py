# import sys
# sys.setrecursionlimit(10 ** 6)
import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, K, As, Bs):
    sum_A = [0]
    max_read_A = 0
    for i in range(N):
        sum_A.append(sum_A[-1] + As[i])
        if sum_A[-1] <= K:
            max_read_A = i + 1
    sum_B = [0]
    max_read_B = 0
    for i in range(M):
        sum_B.append(sum_B[-1] + Bs[i])
        if sum_B[-1] <= K:
            max_read_B = i + 1

    # print(sum_A, max_read_A)
    # print(sum_B, max_read_B)

    ans = 0
    for i in range(max_read_A + 1):
        B_read_time = K - sum_A[i]
        B_read_num = bisect.bisect_right(sum_B, B_read_time) - 1
        ans = max(ans, i + B_read_num)
        # print(i, B_read_num)

    print(ans)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    As = [int(i) for i in input().split()]
    Bs = [int(i) for i in input().split()]

    # import random
    # N, M, K = 200000, 200000, 10 ** 9
    # As = [random.randint(1, 1) for _ in range(N)]
    # Bs = [random.randint(1, 1) for _ in range(M)]
    solve(N, M, K, As, Bs)
