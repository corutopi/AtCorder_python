import sys
sys.setrecursionlimit(10 ** 6)
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, K, ABs, CDs):
    friend_map = [[] for _ in range(N + 1)]
    for a, b in ABs:
        friend_map[a].append(b)
        friend_map[b].append(a)

    block_map = [[] for _ in range(N + 1)]
    for c, d in CDs:
        block_map[c].append(d)
        block_map[d].append(c)

    def dfs(group_num, members, now_n):
        belongs[now_n] = group_num
        members.append(now_n)
        for f in friend_map[now_n]:
            if belongs[f] == -1:
                members = dfs(group_num, members, f)
        return members

    friend_groups = []
    belongs = [-1] * (N + 1)
    for i in range(1, N + 1):
        if belongs[i] == -1:
            m = dfs(len(friend_groups), [], i)
            m.sort()
            friend_groups.append(m)

    ans = ''
    for n in range(1, N + 1):
        block = 0
        group = friend_groups[belongs[n]]
        for b in block_map[n]:
            if belongs[n] == belongs[b]:
                block += 1
        ans += ' ' + str(len(group) - len(friend_map[n]) - block - 1)
    print(ans[1:])


if __name__ == '__main__':
    # # handmade test
    # N, M, K = 2 * 10 ** 5, 10 ** 5, 10 ** 5
    # ABs = [[1, i] for i in range(2, 10 ** 5 + 2)]
    # CDs = [[i, i + 1] for i in range(2, 10 ** 5 + 2)]

    # # handmade random
    # import random
    # N, M, K = 20, 10, 10
    # ABs = []
    # while True:
    #     if len(ABs) == M:
    #         break
    #     a = random.randint(1, N - 1)
    #     b = random.randint(a + 1, N)
    #     if not [a, b] in ABs:
    #         ABs.append([a, b])
    # CDs = []
    # while True:
    #     if len(CDs) == K:
    #         break
    #     c = random.randint(1, N - 1)
    #     d = random.randint(c + 1, N)
    #     if not [c, d] in ABs and not [c, d] in CDs:
    #         CDs.append([c, d])
    # print(N, M, K)
    # print(ABs)
    # print(CDs)

    N, M, K = map(int, input().split())
    ABs = [[int(i) for i in input().split()] for _ in range(M)]
    CDs = [[int(i) for i in input().split()] for _ in range(K)]
    solve(N, M, K, ABs, CDs)
