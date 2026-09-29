# CodeAlpha Internship
# Task 2: Stock Portfolio Tracker

# Stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200
}

# Store portfolio details
portfolio = []

# Total investment
total_investment = 0

print("****************************")
print("     STOCK PORTFOLIO TRACKER")
print("*****************************")

# Ask number of stocks
number = int(input("Enter number of stocks: "))

# Get stock details
for i in range(number):

    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check stock availability
    if stock_name in stocks:

        price = stocks[stock_name]

        # Calculate investment
        investment = price * quantity

        # Add to total
        total_investment = total_investment + investment

        # Store details
        portfolio.append([stock_name, quantity, price, investment])

        print("Stock Price =", price)
        print("Investment =", investment)

    else:
        print("Stock not available!")

# Display final result
print("\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.")
print("          PORTFOLIO")
print("================================")

for item in portfolio:
    print("Stock:", item[0])
    print("Quantity:", item[1])
    print("Price:", item[2])
    print("Investment:", item[3])
    print("----------------------------")

print("Total Investment =", total_investment)

# Save result in CSV file
with open("stock_portfolio.csv", "w") as file:

    file.write("Stock,Quantity,Price,Investment\n")

    for item in portfolio:
        file.write(
            item[0] + "," +
            str(item[1]) + "," +
            str(item[2]) + "," +
            str(item[3]) + "\n"
        )

    file.write("\nTotal Investment," + str(total_investment))

print("\nPortfolio saved successfully in stock_portfolio.csv")