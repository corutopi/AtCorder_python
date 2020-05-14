def solve():
    """
    基本方針:
        a <= b <= c で三角形を作る.
        a, b を決定して取りうる c を計算で求める(O(N ** 2)).
    """
    MAX_LENGTH = 10 ** 3
    N = input()
    L = [int(i) for i in input().split()]
    L.sort()

    # 移動和を求められるようにしておく
    O = [0] * (MAX_LENGTH + 1)
    for l in L:
        O[l] += 1
    O2 = [0] * (MAX_LENGTH + 1)
    for i in range(1, MAX_LENGTH + 1):
        O2[i] = O2[i - 1] + O[i]

    # △カウント
    sum_count = 0
    for i in range(len(L)):
        a = L[i]
        for j in range(i + 1, len(L)):
            b = L[j]
            # c の上限の決定
            c_high = a + b - 1
            if c_high > MAX_LENGTH:
                c_high = MAX_LENGTH
            # △の数加算
            sum_count += O2[c_high] - (j + 1)  # b <= c なので 1 ~ b までの辺を除外
            # print(i, j , O2[c_high] - (j + 1))

    print(sum_count)


if __name__ == '__main__':
    solve()
