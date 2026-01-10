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