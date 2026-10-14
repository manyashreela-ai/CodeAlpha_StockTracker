
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420
}

total_investment = 0
report = []

print("===== STOCK PORTFOLIO TRACKER =====")

n = int(input("How many different stocks do you want to enter? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices and quantity > 0:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        line = (
            f"{stock_name} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}"
        )

        report.append(line)
        print(line)

    else:
        print("Invalid stock name or quantity!")

print("\n===== PORTFOLIO SUMMARY =====")

for item in report:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

with open("stock_portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")

    for item in report:
        file.write(item + "\n")

    file.write(f"\nTotal Investment: ${total_investment}\n")
