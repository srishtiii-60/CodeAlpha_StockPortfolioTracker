# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

n = int(input("\nEnter number of stocks you want to add: "))

portfolio_details = []

for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name} - Quantity: {quantity}, Value: ${investment}"
        )

    else:
        print("Stock not found!")

print("\nPortfolio Summary:")
for item in portfolio_details:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("----------------------\n")

    for item in portfolio_details:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nData saved in portfolio.txt")