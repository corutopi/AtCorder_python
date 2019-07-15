def solve():
    N = int(input())
    W = [int(i) for i in input().split()]
    sumW = sum(W)
    key = 0
    for i in range(len(W)):
        if sumW / 2 < sum(W[:i + 1]):
            key = i
            break
    print(min(abs(sum(W[:key]) - sum(W[key:])),
              abs(sum(W[:key + 1]) - sum(W[key + 1:]))))


if __name__ == '__main__':
    solve()
