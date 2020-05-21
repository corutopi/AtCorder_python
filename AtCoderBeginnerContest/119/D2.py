"""
D - Lazy Faith
"""
# 解説を参考に作成（bisect）
import bisect


def solve():
    # データ読込
    A, B, Q = map(int, input().split())
    si = [-float('inf')] + [int(input()) for i in range(A)] + [float('inf')]
    ti = [-float('inf')] + [int(input()) for i in range(B)] + [float('inf')]
    xi = [int(input()) for i in range(Q)]
    # 問題計算
    for x in xi:
        txi = bisect.bisect_left(ti, x)
        left_t = ti[txi - 1]
        right_t = ti[txi]
        sxi = bisect.bisect_left(si, x)
        left_s = si[sxi - 1]
        right_s = si[sxi]
        print(min(abs(x - min(left_t, left_s)),
                  abs(x - max(right_t, right_s)),
                  abs(x - right_t) + abs(right_t - left_s),
                  abs(x - left_t) + abs(left_t - right_s),
                  abs(x - right_s) + abs(right_s - left_t),
                  abs(x - left_s) + abs(left_s - right_t)))


if __name__ == '__main__':
    solve()
