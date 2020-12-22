import robin_stocks as rs
import os
import getpass
import csv

# Assuming login info is set in environment:
if os.environ.get("robinhood_username") and os.environ.get("robinhood_password"):
    print('Logging in...')
    rs.authentication.login(os.environ.get("robinhood_username"), os.environ.get("robinhood_password"))
    print('Done.')
else:
    # If not, ask for user input for login info:
    print('Robinhood Username: ')
    robinhood_username = input()
    robinhood_password = getpass.getpass('Robinhood Password: ')
    print('Logging in....')
    rs.authentication.login(robinhood_username, robinhood_password)
    print('Done.')

print('Collecting portfolio data...')
portfolio = rs.account.build_holdings(with_dividends=True)
field_names = ['Ticker'] + list(portfolio[list(portfolio)[0]])
positions = rs.account.get_all_positions()
pos_field_names = list(positions[0])

if os.path.exists("rh.csv"):
    os.remove("rh.csv")
with open("rh.csv", 'w', newline='') as rhcsv:
    writer = csv.DictWriter(rhcsv, fieldnames=field_names)
    writer.writeheader()
    for ticker in portfolio:
        row = portfolio[ticker]
        row.update({'Ticker': ticker})
        writer.writerow(row)

rs.export_completed_stock_orders('.')

print('Done. Logging out.')
rs.logout()
