

def solve():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    print(max(N - sum(A), -1))


if __name__ == '__main__':
    solve()
