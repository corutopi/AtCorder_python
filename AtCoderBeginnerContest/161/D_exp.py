# 解説を参考に作成
from collections import deque


def solve(K):
    lunlun = deque([i for i in range(1, 10)])

    ans = 0
    for _ in range(K):
        ans = lunlun.popleft()
        x = ans * 10 + ans % 10
        if x % 10 != 0:
            lunlun.append(x - 1)
        lunlun.append(x)
        if x % 10 != 9:
            lunlun.append(x + 1)

    print(ans)


if __name__ == '__main__':
    K = int(input())
    solve(K)
