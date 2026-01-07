# 1. After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
print("\nExercise 1\n")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total = 0
for i in result:
    if i == "heads":
        total = total + 1
print(f"After flipping a coin 10 times, you got heads a total of {total} times")
#
# # 2. Print square of all numbers between, 1 to 10 except even numbers
print("\nExercise 2\n")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

# 3. Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter an expense amount: ")
e = int(e)
month = -1

for i in range(len(expense_list)):
    if expense_list[i] == e:
        month = i
        break
if month != -1:
    print(f"You spent {e} in {month_list[month]}")
else:
    print(f"You did not spend {e} in any month")

print("\nExercise 3 Improved\n")
# I have updated the expense_list. Notice that I spent 2100 in both March and May.
# month_list = ["January", "February", "March", "April", "May"]
# expense_list = [2340, 2500, 2100, 3100, 2100] # <--- Note the duplicate 2100

# If you run the original code and type 2100, it will only print "March" and then stop.
# The task: Modify the code so that if I enter 2100, it prints: "You spent 2100 in March" AND "You spent 2100 in May"
e = input("Enter an expense amount: ")
e = int(e)
found = False
for i in range(len(expense_list)):
    if expense_list[i] == e:
        print(f'You spent {e} in {month_list[i]}')
        found = True
if not found:
    print(f"You did not spend {e} in any month")

# 4. Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulatory messages.
print("\nExercise 4\n")
km = 1
while km <= 5:
    user_feedback = input(f"Are you tired after {km}km? ")

    if user_feedback == "yes":
        print(f"You didn't finish the race, you stopped at the end of {km}km")
        break
    elif user_feedback == "no":
        km = km + 1
        print(f"Great! Running to  {km} km...")
        if km == 5:
            print(f"Congratulations! You finished the {km}km race")
            break
    else:
        print(f"Please answer with 'yes' or 'no'.")

# 5. The Scenario: The Shopping Cart
# You are building the checkout system for an online store. You have a list of prices for the items in a customer's cart. You need to calculate the Total Bill.
#
# The Rules
# You must use a for loop to go through the list.
#
# You cannot use the cheat code sum(prices) (that's too easy!). You have to do the math yourself inside the loop.
#
# Print the final total at the end.
print("\nExercise 5\n")
cart_prices = [10, 20, 30, 40, 50]
total = 0

for price in cart_prices:
    total += price

print(f"The total cost is: ${total}")

# 6. The Scenario: You have a wallet with only $80. You start adding items to the total one by one.
#
# If adding an item keeps you under or equal to $80, add it.
#
# If adding the next item would make you go over $80, STOP immediately (break) and print "Budget Full!"
# Goal: The loop should add 10, then 20, then 30 (Total 60). When it tries to add 40, it sees that $60 + $40 = $100. That is too high! So it stops. Final Print: Total spent: $60
print("\nExercise 6\n")

cart_prices = [10, 20, 30, 40, 50]
budget = 80
total = 0

for price in cart_prices:
    if total + price > budget:
        print("That is too high! Budget full")
        break
    else:
        total += price
        print(f"You added {price}, total is now {total}")

print(f"The total spent: {total}")