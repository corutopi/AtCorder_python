"""
解説をもとに作成
"""


def solve():
    N = int(input())
    uvw = []
    result = [-1] * N
    for i in range(N - 1):
        lst = [int(i) for i in input().split()]
        uvw.append([lst[0],
                    lst[1],
                    lst[2]])
    # 木の頂点を求める
    # -> 任意の場所で良い. 1 とする.
    # 頂点から順に塗っていく
    result[0] = False
    result, uvw = paint(uvw, 1, result)
    for i in result:
        print(int(i))


def paint(uvw, num, result):
    import pprint
    target_uvw = []
    '''num につながる枝のデータを抽出'''
    # print('頂点 {} について探索'.format(num))
    for t in uvw:
        # print(t)
        if t[0] == num or t[1] == num:
            target_uvw.append(t)
    # print('探索対象 {} 件'.format(len(target_uvw)))
    # pprint.pprint(target_uvw)
    '''次につながる頂点をすべて検索して色塗り'''
    next_nums = []
    for t in target_uvw:
        uvw.remove(t)
        target = t[0] if t[0] != num else t[1]
        result[target - 1] = result[num - 1] if t[2] % 2 == 0 else not (
        result[num - 1])
        next_nums.append(target)
    '''次の頂点データについて検索を行う'''
    for nn in next_nums:
        result, uvw = paint(uvw, nn, result)
    return result, uvw


if __name__ == '__main__':
    solve()
