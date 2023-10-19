# Dictionary
new_dictionary = {}

# adding key:pairs to the dictionary
new_dictionary["a1"] = "X"
new_dictionary["b1"] = "O"
new_dictionary["c1"] = "O"
new_dictionary["a2"] = " "
new_dictionary["b2"] = " "
new_dictionary["b3"] = " "
new_dictionary["c1"] = " "
new_dictionary["c2"] = "O"
new_dictionary["c3"] = " "

# accessing pairs by key
# print(new_dictionary['c1'])


# List example
new_list = [1, 2, 3]

# print(new_list[1])

# new_list = ["oranges", 2, True]

# adds an item at the end of a list
"""
new_list.append("1")
print(new_list)

new_list = [["oranges", 2, True], ["oranges", 2, True], ["oranges", 2, True]]

print(new_list)
"""

ttt = [
    ["1", "2", "3", "4", "5"],
    ["L2 1", "L2 2", "L2 3", "L2 4", "L2 5"],
    ["x", "y", "z", "j", "k"]
]

"""
for i in ttt:
    for j in i:
        print(j, end="")
    print("")
"""

for i in range(0, 3):
    for j in range(0, 5):
        print(ttt[i][j], end="")
    print("")
