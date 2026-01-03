# 1. Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
exp=[2200,2350,2600,2130,2190]

# i. In Feb, how many dollars you spent extra compare to January?
print("In feb, ", exp[1]-exp[0], "dollars was spent compared to Jan")

# ii. Find out your total expense in first quarter (first three months) of the year.
print("Total expenses for the first quarter is:", exp[0]+exp[1]+exp[2])

# iii. Find out if you spent exactly 2000 dollars in any month
2000 in exp
# ans. False

# iv. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)

# v. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3]= exp[3]-200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]


# 2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# i. Length of the list
len(heros)

# ii. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = "doctor strange"
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)