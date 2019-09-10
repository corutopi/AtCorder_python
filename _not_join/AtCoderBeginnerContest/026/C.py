

def solve():
    N = int(input())
    B = [0, 0]
    for i in range(N - 1):
        B.append(int(input()))

    def x(s_num):
        buka = []
        for i in range(len(B)):
            if B[i] == s_num:
                buka.append(x(i))
        if len(buka) == 0:
            return 1
        else:
            return max(buka) + min(buka) + 1

    print(x(1))


if __name__ == '__main__':
    solve()
