import timeit
import time

def rec_mc(coin_list, change):
    min_coins = change
    if change in coin_list:
        return 1
    else:
        for value in [coin for coin in coin_list if coin <= change]:
            num_coins = 1 + rec_mc(coin_list, change - value)
            if num_coins < min_coins:
                min_coins= num_coins
    return min_coins

def rec_mc_with_memoization(coin_list, change, known_values):
    '''
    coin_list - List of valid denominations of coins
    known_values - dictionary of denominations and number of coins needed.
    change - amount for which required number of coins is calculated
    '''
    min_coins = change
    if change in coin_list:
        known_values[change] = 1
        return 1
    if known_values[change] > 0:
        return known_values[change]
    for value in [coin for coin in coin_list if coin <= change]:
        num_coins = 1 + rec_mc_with_memoization(coin_list, change-value, known_values)
        if num_coins < min_coins:
            min_coins = num_coins
            known_values[change] = min_coins
    return min_coins

def dp_mc(coin_list, change):
    coins_used_list = [0]*(change+1)
    min_coins_list = [0]*(change+1)
    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for coin_val in [coin for coin in coin_list if coin <= cents]:
            if min_coins_list[cents-coin_val] + 1 < coin_count:
                coin_count = min_coins_list[cents-coin_val] + 1
                new_coin = coin_val
        min_coins_list[cents] = coin_count
        coins_used_list[cents] = new_coin
    return min_coins_list[change], get_used_coins(coins_used_list=coins_used_list, change=change) 

def get_used_coins(coins_used_list, change):
    coin = change
    all_coins_list = []
    while coin > 0:
        used_coin = coins_used_list[coin]
        all_coins_list.append(used_coin)
        coin = coin - used_coin
    return all_coins_list



if __name__ == "__main__":
    # cur_time = time.time()
    # print(f"Required number of coins without caching:{rec_mc(coin_list=[1,5,10,25], change=63)}, execution_time={time.time() - cur_time}")
    cur_time = time.time()
    print(f"Required number of coins with caching:{rec_mc_with_memoization(coin_list=[1,5,10,25], change=63, known_values=[0]*64)}, execution_time={time.time() - cur_time}")
    cur_time = time.time()
    num_coins, coins = dp_mc(coin_list=[1,5,10,25], change=63)
    print(f"Required number of coins with dynamic programming:{num_coins}, used_coins={coins} execution_time={time.time() - cur_time}")