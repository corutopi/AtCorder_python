def solve():
    L = int(input(), 2)
    mm = 10 ** 9 + 7
    # 0000 ... との組み合わせの数
    sum0 = L * 2 % mm
    # 1111 ... との組み合わせの数
    import math
    l2 = int(math.log2(L))
    for i in range(0, l2):
        base1 = int(2 ** (l2 - 1))
        base2 = 2 ** l2
        a = (base2 - base1)
        pass
    print(sum0)



if __name__ == '__main__':
    solve()
