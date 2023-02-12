"""
提出 #6475942 を参考に作成
"""

import bisect


def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    color_list = [A[-1]]
    for a in reversed(A[:-1]):
        # a より大きい数の中で一番小さい数の場所を取得する
        c = bisect.bisect_left(color_list, a + 1)
        if c == len(color_list):
            color_list.append(a)
        else:
            color_list[c] = a
    print(len(color_list))


if __name__ == '__main__':
    solve()
