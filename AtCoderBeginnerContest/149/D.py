# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, R, S, P, T):
    k_list = [[] for _ in range(K)]
    for i in range(len(T)):
        k_list[i % K].append(T[i])

    ans = 0
    for kl in k_list:
        dp = [[0, 0, 0] for _ in range(len(kl) + 1)]
        for i in range(len(kl)):
            # rock
            dp[i + 1][0] = max(dp[i][1], dp[i][2])
            dp[i + 1][0] += R if kl[i] == 's' else 0
            # scissors
            dp[i + 1][1] = max(dp[i][0], dp[i][2])
            dp[i + 1][1] += S if kl[i] == 'p' else 0
            # paper
            dp[i + 1][2] = max(dp[i][0], dp[i][1])
            dp[i + 1][2] += P if kl[i] == 'r' else 0
        ans += max(dp[-1])

    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # N, K = 10 ** 5, 10 ** 3
    # R, S, P = 100, 90, 5
    # T = 'r' * 10 ** 5

    solve(N, K, R, S, P, T)
