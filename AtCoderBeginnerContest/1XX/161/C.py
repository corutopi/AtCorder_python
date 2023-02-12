

def solve(N, K):
    if N > K:
        N = N % K
    print(min(N, abs(N - K)))


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N ,K)
