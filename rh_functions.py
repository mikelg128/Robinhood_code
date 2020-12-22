import os
import robin_stocks as rs
import getpass
import csv
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

print("If this is a new session, make sure to run login() before executing any other commands")

def login():
    if os.environ.get("robinhood_username") and os.environ.get("robinhood_password"):
        print('Logging in....')
        rs.authentication.login(os.environ.get("robinhood_username"), os.environ.get("robinhood_password"))
        print('Done.')
    else:
        # If not, ask for user input for login info:
        print('Robinhood Username: ')
        robinhood_username = input()
        robinhood_password = getpass.getpass('Robinhood Password: ')  # WARNING: Echoes in Python terminal
        print('Logging in....')
        rs.authentication.login(robinhood_username, robinhood_password)
        print('Done. You are now logged in for 1 day or for this session. Use rs.logout() to logout manually.')


def export_holdings():
    print('Collecting portfolio data...')
    portfolio = rs.account.build_holdings(with_dividends=True)
    field_names = ['symbol'] + list(portfolio[list(portfolio)[0]])
    filename = 'rh.csv'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w', newline='') as rhcsv:
        writer = csv.DictWriter(rhcsv, fieldnames=field_names)
        writer.writeheader()
        for ticker in portfolio:
            row = portfolio[ticker]
            row.update({'symbol': ticker})
            writer.writerow(row)
    print('Done.')
    return portfolio, filename


def export_order_history():
    print('Exporting order history to stock_orders_{}.csv'.format(date.today().strftime('%b-%d-%Y')))
    rs.export_completed_stock_orders('.')
    print('Done')
    return "stock_orders_{}.csv".format(date.today().strftime('%b-%d-%Y'))


def find_ticker_info(ticker, filename):
    info = []
    with open(filename, 'r', newline='') as rhcsv:
        reader = csv.DictReader(rhcsv)
        for row in reader:
            if row['symbol'] == ticker:
                print(row)
                info.append(row)
    return info


def plot_purchased_equity_history(ticker, filename):
    filename = "stock_orders_{}.csv".format(date.today().strftime('%b-%d-%Y'))
    info = []
    with open(filename, 'r', newline='') as rhcsv:
        reader = csv.DictReader(rhcsv)
        for row in reader:
            if row['symbol'] == ticker:
                print(row)
                info.append(row)

    datetime = []
    price = []
    for x in info:
        datetime.append(x['date'])
        price.append(x['average_price'])

    df = pd.DataFrame(data={'Time': datetime, 'Average Price': price}, index=0)
    print(df)

