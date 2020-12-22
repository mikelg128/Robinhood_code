import os
import getpass
import robin_stocks as rs

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
