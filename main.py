risk = 5
rr = 5
stop = 2
target = stop*rr
multiple = risk/5
trade_num = 10
success = 1


risk_table="Strike rate (%)", "Return over " + str(trade_num) + " trades"
print(risk_table)
while success < 10:
  win = 1 + 0.1*target*multiple
  loss = 1 - multiple*(0.1*stop)
  val = win**success * loss**(trade_num-success)
  roi = (val-1)*100
  print(success*10,round(roi))
  success += 1




