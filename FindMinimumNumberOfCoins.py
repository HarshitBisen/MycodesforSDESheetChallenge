denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    count=0
    for i in range(8,-1,-1):
        if amount/denominations[i]>=1:
            count+=amount//denominations[i]
            amount=amount%denominations[i]
        if amount==0:
            break;
    return count
