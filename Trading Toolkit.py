
running = True

while running:        
    print("===========================")
    print("      TRADING TOOLKIT")
    print("===========================")
    print("1. Pip Calculator")
    print("2. Risk Calculator")
    print("3. Position Size Calculator")
    print("4. Stop Loss Calculator")
    print("5. Exit")
    print("===========================")
    choice = input("Choose an Option: ")

    if choice == "1":
        # Pip Calculator
        print("===========================")
        print("    TRADING PIP CALCULATOR")
        print("===========================")

        currency_pair = input("Enter Currency Pair (e.g. EUR/USD, GBP/USD, XAU/USD): ")
        lot_size = float(input("Enter Lot Size (e.g. 0.01, 0.10, 1.00): "))
        pips = float(input("Enter Number of Pips: "))
        trade_type = input("Trade Type (Buy/Sell): ").strip().lower()

        # Simplified pip value calculation
        pip_value = lot_size * 10
        profit_loss = pip_value * pips

        print("\n========== RESULT ==========")
        print("Currency Pair:", currency_pair)
        print("Trade Type:", trade_type.title())
        print("Lot Size:", lot_size)
        print("Pips:", pips)
        print("Value Per Pip: ${:.2f}".format(pip_value))
        print("Profit/Loss: ${:.2f}".format(profit_loss))
        print("============================")

    elif choice == "2":
        # Risk Calculator
        print("===========================")
        print("      RISK CALCULATOR")
        print("===========================")

        account_balance = float(input("Enter Account Balance: $"))
        risk_percent = float(input("Enter Risk Percentage (%): "))

        risk_amount = account_balance * (risk_percent / 100)

        print("\n========== RESULT ==========")
        print("Account Balance: ${:.2f}".format(account_balance))
        print("Risk Percentage: {}%".format(risk_percent))
        print("Amount to Risk: ${:.2f}".format(risk_amount))
        print("============================")

    elif choice == "3":
        print("Position Size Calculator (Coming Soon)")

    elif choice == "4":
        print("Stop Loss Calculator (Coming Soon)")

    elif choice == "5":
        print("Goodbye!")
        running = False

    else:
        print("Invalid Choice. Please try again.")