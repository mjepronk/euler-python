# vim: sw=4:ts=4:et:ai

def num_combinations(coins, target, amount=0, prev_coin=None):
    num_combs = 0
    rest = target - amount
    for coin in coins:
        if prev_coin and coin < prev_coin:
            break
        if coin == rest:
            num_combs += 1
        elif coin < rest:
            num_combs += num_combinations(coins, target, amount + coin, coin)
        else:
            continue
    return num_combs

def main():
    target_amount = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coins.sort(reverse=True)
    return num_combinations(coins, target_amount)

if __name__ == '__main__':
    print("Result: %i" % main())

