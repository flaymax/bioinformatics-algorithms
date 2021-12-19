def TheChangeProblem(money,Coins , a = {}):
    res = [(money//i) for i in Coins if (money%i == 0)]
    while money != 0:
        M = max(Coins)
        a[M] = money // M
        money %= M
        Coins.remove(M)
    return [sum(a.values())] + res 

with open("rosalind_ba5a.txt") as f:
    money = int(f.readline().strip())
    Coins = [int(l) for l in f.readline().strip().split(",")]
    print(Coins)
f.close()
print(min(TheChangeProblem(money, Coins)))