import os
import robin_stocks as rs
import getpass
import csv


def import_modules():  # quickly import when starting a console session
    import os
    import robin_stocks as rs
    import getpass
    import csv


def rh_login():
    if os.environ.get("robinhood_username") and os.environ.get("robinhood_password"):
        print('Logging in....')
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


def rh_build_holdings():
    print('Collecting portfolio data...')
    portfolio = rs.account.build_holdings(with_dividends=True)
    field_names = ['Ticker'] + list(portfolio[list(portfolio)[0]])

    if os.path.exists("rh.csv"):
        os.remove("rh.csv")
    with open("rh.csv", 'w', newline='') as rhcsv:
        writer = csv.DictWriter(rhcsv, fieldnames=field_names)
        writer.writeheader()
        for ticker in portfolio:
            row = portfolio[ticker]
            row.update({'Ticker': ticker})
            writer.writerow(row)


def rh_export_order_history():
    rs.export_completed_stock_orders('.')
