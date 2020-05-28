def solve(K, N, As):
    longest = 0
    for i in range(len(As)):
        x = 0
        if i == len(As) - 1:
            x = As[0] + (K - As[i])
        else:
            x = As[i + 1] - As[i]
        longest = max(longest, x)
    print(K - longest)


if __name__ == '__main__':
    K, N = map(int, input().split())
    As = [int(a) for a in input().split()]
    solve(K, N, As)
