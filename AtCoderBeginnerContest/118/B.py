"""
Foods Loved by Everyone
"""


def solve():
    pass
    '''初期値設定'''
    N, M = [int(i) for i in input().split()]
    food = [0 for i in range(M + 1)]
    '''好み調査開始'''
    for i in range(N):
        p = [int(m) for i, m in enumerate(input().split()) if i != 0]
        for f in p:
            food[f] += 1
    '''結果出力'''
    print(food.count(N))


if __name__ == '__main__':
    solve()
