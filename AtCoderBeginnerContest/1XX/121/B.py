"""
B - Can you solve this?
2回目. 型アノテーションがはじかれるの忘れてた
"""


def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for n in range(N):
        A = list(map(int, input().split()))
        AB = [A[i] * B[i] for i in range(len(A))]
        if sum(AB) + C > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
