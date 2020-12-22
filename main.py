import robin_stocks as rs
import os

# Assuming login info is set in environment:
rs.authentication.login(os.environ.get("robinhood_username"), os.environ.get("robinhood_password"))

portfolio = rs.account.build_holdings(with_dividends=True)

print("Ticker   Qty Shares  Equity")
for x in portfolio:
    print(x, "  ", portfolio[x].get("quantity"), "  ", portfolio[x].get("equity"))

rs.logout()