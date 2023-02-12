def solve():
    N = int(input())
    uvw = []
    w = []
    result = [-1] * N
    for _ in range(N - 1):
        lst = [int(i) for i in input().split()]
        uvw.append([lst[0] if lst[0] <= lst[1] else lst[1],
                    lst[1] if lst[0] <= lst[1] else lst[0],
                    lst[2]])
    uvw.sort()
    # print(uvw)
    # 木の頂点を求める
    # -> 任意の場所で良い. 1 とする.
    # 頂点から順に塗っていく
    result[0] = False
    result = paint(uvw, 1, result)
    for i in result:
        print(int(i))


def paint(uvw, num, result):
    target_uvw = []
    for t in uvw:
        if t[0] == num or t[1] == num:
            target_uvw.append(t)
            uvw.remove(t)
    next_nums = []
    for t in target_uvw:
        target = t[0] if t[0] != num else t[1]
        result[target - 1] = result[num - 1] if t[2] % 2 == 0 else not(result[num - 1])
        next_nums.append(target)
    # print('探索中の番号:', num)
    # print('ヒットしたデータ', target_uvw)
    # print('現在の結果', result)
    for nn in next_nums:
        result = paint(uvw, nn, result)
    return result


if __name__ == '__main__':
    solve()
