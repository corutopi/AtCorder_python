"""
解説を参考に作成 その3
"""


def solve():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort()
    CB = [list(reversed([int(i) for i in input().split()])) for _ in range(M)]
    CB = list(sorted(CB, reverse=True))

    count = 0
    flag = False
    for cb in CB:
        for b in range(cb[1]):
            if A[count] < cb[0]:
                A[count] = cb[0]
            else:
                flag = True
                break
            count += 1
            if count >= N:
                flag = True
                break

        if flag:
            break
    print(sum(A))


if __name__ == '__main__':
    solve()
