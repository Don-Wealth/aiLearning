# 1. We have the following information on countries and their population (population is in crores),
#
# Country	Population
# China	    143
# India	    136
# USA	    32
# Pakistan	21
# i.Using above create a dictionary of countries and its population
countries = {"china" : 143, "india" : 136, "usa" : 32, "pakistan": 21}

# ii. Write a program that asks user for three type of inputs,
#   a. print: if user enter print then it should print all countries with their population in this format,
    # china==>143
    # india==>136
    # usa==>32
    # pakistan==>21

    # b. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

    # c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

    # d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

# solution
command = input("Enter command (print, add, remove, query): ").lower()

#   --- OPERATION A: PRINT ---
if command == "print":
    for country, population in countries.items():
        print(f"{country.lower()}==>{population}")

#   --- OPERATION B: ADD ---
elif command == "add":
    country_to_add = input("Enter a country name to add: ").lower()

    if country_to_add in countries:
        print("Country already exists!")
    else:
        pop_to_add = int(input(f"Enter population for {country_to_add}: "))
        countries[country_to_add] = pop_to_add
        print("Country added!")
        print(countries)

# --- OPERATION C: REMOVE ---
elif command == "remove":
    country_to_remove = input("Enter a country name to remove: ").lower()
    if country_to_remove in countries:
        del countries[country_to_remove]
        print("Country removed!")

        for country, population in countries.items():
            print(f"{country.lower()}==>{population}")
        else:
            print("Country not found!")

# --- OPERATION D: QUERY ---
elif command == "query":
    country_to_query = input("Enter a country name to lookup: ").lower()
    if country_to_query in countries:
        print(f"Population for {country_to_query} is: {countries[country_to_query]}")
    else:
        print("Country not found in database.")

else:
    print("Invalid command!")


# 2. You are given following list of stocks and their prices in last 3 days,
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# i. Write a program that asks user for operation. Value of operations could be,
#       a. print: When user enters print it should print following,
#       info == > [600, 630, 620] == > avg: 616.67
#       ril == > [1430, 1490, 1567] == > avg: 1495.67
#       mtl == > [234, 180, 160] == > avg: 191.33
#
#       b. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

# SOLUTION
stocks = {
    "info" : [600, 630, 620],
    "rill" : [1430, 1490, 1567],
    "mtl"  : [234, 180, 160]
}
operation_input = input("Enter operation (print, add): ").lower()

#   ---OPERATION A: PRINT---
if operation_input == "print":
    for stock, price in stocks.items():
        # calculate avg
        avg_price = sum(price) / len(price)
        print(f"{stock.lower()} == > {price} == > avg: {avg_price}")

#   ---OPERATION B: ADD---
elif operation_input == "add":
    stock_to_add = input("Enter a stock name to add: ").lower()
    if stock_to_add in stocks:
        append_to_list = int(input(f"stock already exists for {stock_to_add}. Add a price to the list: "))
        stocks[stock_to_add].append(append_to_list)
        print(f"New price {append_to_list} added to Stocks. \n {stocks} ")
    else:
        raw_input = input(f"Enter price for {stock_to_add} separated by comma:")
        try:
            price_list_string = raw_input.split(",")
            final_price_list = [int(price) for price in price_list_string]
            stocks[stock_to_add] = final_price_list
            print("Stock added!")
            print(stocks)
        except ValueError:
            print("Please make sure you use commas and only enter numbers (no letters!).")

else:
    print("Invalid command!")