# 解説を参考に作成


def solve():
    N, K, C = map(int, input().split())
    S = input()

    left = []
    rest = 0
    work = 0
    for i in range(N):
        if S[i] == 'o' and rest == 0:
            left.append(i)
            rest = C + 1
            work += 1
        if rest > 0:
            rest -= 1
        if work == K:
            break

    right = []
    rest = 0
    work = 0
    for i in reversed(range(N)):
        if S[i] == 'o' and rest == 0:
            right.append(i)
            rest = C + 1
            work += 1
        if rest > 0:
            rest -= 1
        if work == K:
            break
    right = list(reversed(right))

    # print(left)
    # print(right)
    for i in range(len(left)):
        if left[i] == right[i]:
            print(left[i] + 1)


if __name__ == '__main__':
    solve()
