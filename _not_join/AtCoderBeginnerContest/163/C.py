def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = [0] * N
    for Ai in A:
        ans[Ai - 1] += 1
    for a in ans:
        print(a)


if __name__ == '__main__':
    solve()



