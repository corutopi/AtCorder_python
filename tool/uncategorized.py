def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


def binary_search_double(ok, ng, solve, cnt=100):
    """めぐる式2分探索"""
    for _ in range(cnt):
        mid = (ok + ng) / 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


def slide_minimum(l, k):
    """スライド最小値のlistを返す

    :param l: list
    :param k: min(l[i] ... l[i + k])
    :return:
    """
    from collections import deque
    dq = deque([])
    for i in range(k):
        while dq and l[dq[-1]] > l[i]:
            dq.pop()
        dq.append(i)
    re = []
    for i in range(len(l)):
        if i + k < len(l):
            while dq and l[dq[-1]] > l[i + k]:
                dq.pop()
            dq.append(i + k)
        if dq[0] == i - 1:
            dq.popleft()
        re.append(l[dq[0]])
    return re


def slide_maximum(l, k):
    """スライド最大値のlistを返す.
    O(len(l))

    :param l: list
    :param k: min(l[i] ... l[i + k])
    :return:
    """
    from collections import deque
    dq = deque([])
    for i in range(k):
        while dq and l[dq[-1]] < l[i]:
            dq.pop()
        dq.append(i)
    re = []
    for i in range(len(l)):
        if i + k < len(l):
            while dq and l[dq[-1]] < l[i + k]:
                dq.pop()
            dq.append(i + k)
        if dq[0] == i - 1:
            dq.popleft()
        re.append(l[dq[0]])
    return re


def slide_maximum_2d(l, h, w):
    """2次元配列のスライド最大値のlistを返す.
    各 l[i][j] 毎に, l[i][j], l[i + h][j + w]を頂点とする長方形内部での最大値を持つ2次元配列を作る.
    計算量: O(len(l)*len(l[i])

    :param l:
    :param h:
    :param w:
    :return:
    """
    from collections import deque
    H, W = len(l), len(l[0])
    re = []

    # 横方向の計算(slide_maximum 使ってもいいかもしれない)
    for li in l:
        x = []
        dq = deque([])
        for j in range(w):
            while dq and li[dq[-1]] < li[j]:
                dq.pop()
            dq.append(j)
        for j in range(W):
            if j + w < W:
                while dq and li[dq[-1]] < li[j + w]:
                    dq.pop()
                dq.append(j + w)
            if dq[0] == j - 1:
                dq.popleft()
            x.append(li[dq[0]])
        re.append(x)

    # 縦方向の計算
    for j in range(len(l[0])):
        dq = deque([])
        for i in range(h):
            while dq and re[dq[-1]][j] < re[i][j]:
                dq.pop()
            dq.append(i)
        for i in range(H):
            if i + h < H:
                while dq and re[dq[-1]][j] < re[i + h][j]:
                    dq.pop()
                dq.append(i + h)
            if dq[0] == i - 1:
                dq.popleft()
            re[i][j] = re[dq[0]][j]

    return re


def coordinate_compression(x, start=0):
    """整数のリストを座標圧縮したものを返す.デフォルトの最小値0.

    :param x: integer list
    :param start:
    :return:
    """
    xd = {v: i + start for i, v in enumerate(sorted(x))}
    return list(map(lambda d: xd[d], x))


if __name__ == '__main__':
    # print(slide_minimum([9, 8, 7, 6, 5, 4, 3, 2, 1], 1))
    # print(slide_minimum([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    # print(slide_maximum([9, 8, 7, 6, 5, 4, 3, 2, 1], 1))
    # print(slide_maximum([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    # l = [[i * j for j in range(10)] for i in range(10)]
    # [print(l2) for l2 in l]
    # print('--------')
    # [print(sm) for sm in slide_maximum_2d(l, 2, 3)]
    pass
