

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = A.copy()
    for i in reversed(range(1, N // 2 + 1)):
        tag = i * 2
        tmp = 0
        while tag <= N:
            tmp += ans[tag - 1]
            tag += i
        ans[i - 1] = 1 if tmp % 2 != ans[i - 1] else 0

    print(sum(ans))
    s = ''
    for i, a in enumerate(ans, 1):
        if a == 1:
            s += str(i) + ' '
    if s != '':
        print(s.strip())


if __name__ == '__main__':
    solve()
