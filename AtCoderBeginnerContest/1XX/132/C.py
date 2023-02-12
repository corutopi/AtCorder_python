

def solve():
    N = int(input())
    D = [int(i) for i in input().split()]
    D.sort()
    print(D[N // 2] - D[(N // 2) - 1])


if __name__ == '__main__':
    solve()
