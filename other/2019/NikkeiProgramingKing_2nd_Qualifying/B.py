

def solve():
    N = int(input())
    D = [int(i) for i in input().split()]
    # 対象となる木のパターン数のチェック
    mD = max(D)
    nD = [0] * (mD + 1)
    for d in D:
        nD[d] += 1
    # 頂点が1でなくてはならない
    if D[0] != 0:
        print(0)
        return
    # 頂点が複数あってはならない
    if nD[0] != 1:
        print(0)
        return
    count = nD[0]
    for i in range(2, len(nD)):
        count *= nD[i - 1] ** nD[i]
        count = count % 998244353
    print(count)


if __name__ == '__main__':
    solve()
