buy_price1 = float(input("Enter buy price for first purchase: "))
shares_bought1 = int(input("Enter number of shares bought for first purchase: "))

sell_price1 = float(input("Enter sell price for first sale: "))
shares_sold1 = int(input("Enter number of shares sold for first sale: "))
sell_price2 = float(input("Enter sell price for second sale: "))
shares_sold2 = int(input("Enter number of shares sold for second sale: "))

buy_price2 = float(input("Enter buy price for second purchase: "))
shares_bought2 = int(input("Enter number of shares bought for second purchase: "))
sell_price3 = float(input("Enter sell price for third sale: "))

buy_commission = 0.035
sell_commission = 0.025
interest = 0.075


total_bought = buy_price1 * shares_bought1
total_buy_commission = total_bought * buy_commission

total_sold1 = sell_price1 * shares_sold1
total_sold2 = sell_price2 * shares_sold2
total_sell_commission = (total_sold1 + total_sold2) * sell_commission

cost1 = total_bought + total_buy_commission + total_sell_commission
total_profit1 = total_sold1 + total_sold2 - cost1


total_bought2 = buy_price2 * shares_bought2
total_buy_commission2 = total_bought2 * buy_commission
total_interest = total_bought2 * interest

total_sold3 = sell_price3 * shares_bought2
total_sell_commission2 = total_sold3 * sell_commission

cost2 = (total_bought2 + total_buy_commission2 + total_sell_commission2 + total_interest)
total_profit2 = total_sold3 - cost2


total_commission = total_buy_commission + total_buy_commission2 + total_sell_commission + total_sell_commission2
overall_profit = total_profit1 + total_profit2
initial_investment = total_bought + total_bought2
percentage_gain = overall_profit/initial_investment * 100


print(f"\nTotal commission paid is ${total_commission:,.2f}")
print(f"Profit from the first trade is ${total_profit1:,.2f}")
print(f"Profit from the second trade is ${total_profit2:,.2f}")
print(f"Overall profit is ${overall_profit:,.2f}")

if percentage_gain > 5:
    print(f"Good investment, total percentage gain was {percentage_gain:,.3f}%")
else:
    print(f"Bad investment, total percentage gain was only {percentage_gain:,.3f}%")