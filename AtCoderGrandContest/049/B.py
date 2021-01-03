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
def solve(N, S, T):
    S1_cumsum_rev = [0]
    T1_cumsum_rev = [0]
    S1_point = []
    T1_point = []
    # impossible when S1 < T1 of '1' count.
    # impossible when S1sum(S[:i]) < T1sum(T[:i]).
    for i in range(N):
        S1_cumsum_rev.append(S1_cumsum_rev[-1] + int(S[N - i - 1]))
        T1_cumsum_rev.append(T1_cumsum_rev[-1] + int(T[N - i - 1]))
        if T1_cumsum_rev[-1] > S1_cumsum_rev[-1]:
            print(-1)
            return
        if S[i] == '1':
            S1_point.append(i)
        if T[i] == '1':
            T1_point.append(i)
    # impossible when (S1 - T1) % 2 == 1.
    if (T1_cumsum_rev[-1] - S1_cumsum_rev[-1]) % 2 == 1:
        print(-1)
        return

    # main
    # S, T の最初の1の位置を記録.
    ans = 0
    si = 0
    ti = 0
    Sdel = None
    T1_point.append(inf)  # prevention out of range
    while si < len(S1_point):
        # Sdel に場所が記録されている場合は S' と合わせて削除する
        if Sdel is not None:
            ans += S1_point[si] - Sdel
            Sdel = None
            # # そして次のSの1の場所を検索してS'に指定する.
            si += 1
            continue
        if T1_point[ti] <= S1_point[si]:
            # # T' <= S' の場合, T' の位置まで S' を移動させる.
            ans += S1_point[si] - T1_point[ti]
            # # そして次の1の場所をS,Tそれぞれで検索して指定する.
            si += 1
            ti += 1
            continue
        else:
            # # T' > S' の場合, 削除すべき S' として場所を記録(Sdel)する.
            Sdel = S1_point[si]
            # # そして次のSの1の場所を検索してS'に指定する.
            si += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    S = input()
    T = input()
    solve(N, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10
    # while True:
    #     S = random_str(N, '01')
    #     T = random_str(N, '01')
    #     solve(N, S, T)
