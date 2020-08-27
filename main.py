#% of the account risked per trade
risk = 5
#Dollars made per dollar risked
rr = 5
#% distance until stop loss is executed
stop = 2
#% distance until target is reached
target = stop * rr
#used to calulate what % of the total account should be placed in a 10x leveraged position
multiple = risk / 5
#number of trades taken
trade_num = 10
#number of winning trades
success = 1

risk_table = "Strike rate (%)", "Return over " + str(trade_num) + " trades"
print(risk_table)
while success < 10:
    win = 1 + 0.1 * target * multiple
    loss = 1 - multiple * (0.1 * stop)
    val = win**success * loss**(trade_num - success)
    roi = (val - 1) * 100
    print(success * 10, round(roi))
    success += 1
