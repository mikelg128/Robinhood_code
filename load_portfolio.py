import csv


def load_portfolio():
    # Loads portfolio from csv
    portfolio = dict()
    with open("rh.csv", 'r', newline='') as rhcsv:
        reader = csv.DictReader(rhcsv)
        for row in reader:
            ticker = str(row['Ticker'])
            del row['Ticker']
            portfolio.update({ticker: row})
            print(ticker + ': ' + portfolio[ticker]['equity'])

    return portfolio


if __name__ == "__main__":
    portfolio = load_portfolio()
