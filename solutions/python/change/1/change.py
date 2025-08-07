def find_fewest_coins(coins, target):
    if target == 0:
        return []
    if target < 0:
        raise ValueError("target can't be negative")
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    backtrack = [-1] * (target + 1)
    for i in range(1, target + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                backtrack[i] = c
        #print(backtrack)
    curr = target
    used_coins = []
    while curr > 0:
        coin = backtrack[curr]
        if coin == -1:
            break  # no solution
        used_coins.append(coin)
        curr -= coin
    if not used_coins:
        raise ValueError("can't make target with given coins")
    return used_coins
#print(find_fewest_coins([1, 5, 10, 21, 25], 0))
