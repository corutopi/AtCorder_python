import math


def solve():
    A, B, C, D = map(int, input().split())

    takagi = math.ceil(C / B)
    aoki = math.ceil(A / D)

    # print(takagi, ':', aoki)
    if takagi <= aoki:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
