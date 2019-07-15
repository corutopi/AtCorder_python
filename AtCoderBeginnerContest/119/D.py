"""
D - Lazy Faith
"""


def solve():
    # データ読込
    A, B, Q = map(int, input().split())
    shrines = [int(input()) for i in range(A)]
    temple = [int(input()) for i in range(B)]
    question = [int(input()) for i in range(Q)]
    # 問題計算
    for q in question:
        t_list = []
        # 寺から神社に行くときの計算
        t_s = 0
        abs_temple = [abs(q - t) for t in temple]
        target = abs_temple.index(min(abs_temple))
        t_temple = temple[target]
        t_s += abs(q - t_temple)
        abs_shrines = [abs(t_temple - s) for s in shrines]
        t_s += min(abs_shrines)
        t_list.append(t_s)
        if abs_temple.count(min(abs_temple)) > 1:
            # 同じ距離の寺が二つあるときの考慮
            t_s2 = 0
            t_temple = temple[target + 1]
            t_s2 += abs(q - t_temple)
            abs_shrines = [abs(t_temple - s) for s in shrines]
            t_s2 += min(abs_shrines)
            t_list.append(t_s2)
        # 神社から寺に行くときの計算
        s_t = 0
        abs_shrines = [abs(q - s) for s in shrines]
        target = abs_shrines.index(min(abs_shrines))
        t_shrines = shrines[target]
        s_t += abs(q - t_shrines)
        abs_temple = [abs(t_shrines - t) for t in temple]
        s_t += min(abs_temple)
        t_list.append(s_t)
        if abs_shrines.count(min(abs_shrines)) > 1:
            # 同じ距離の寺が二つあるときの考慮
            s_t2 = 0
            t_shrines = shrines[target + 1]
            s_t2 += abs(q - t_shrines)
            abs_temple = [abs(t_shrines - t) for t in temple]
            s_t2 += min(abs_temple)
            t_list.append(s_t2)
        # 出力
        print(min(t_list))


if __name__ == '__main__':
    solve()
