import random

#len()
""" print(f"We have {len(shopping_list)} items on the list.") """

#append()
""" shopping_list.append(["flour", "sugar", "baking powder"]) """

#extend()
""" shopping_list.extend(["flour", "sugar", "baking powder"]) """

#remove()
""" shopping_list.remove("cheese") """

""" for item in shopping_list.copy():
    if item == "cheese":
        shopping_list.remove(item) """

#count()
""" n = shopping_list.count("cheese")

print(f"There are {n} instances of cheese on the list.") """

#index()
""" apple_index = shopping_list.index("apples")
shopping_list[apple_index] = "bananas" """

# item in
""" found = "milk" in shopping_list """

""" for item in shopping_list:
    if item == "soy milk":
        found = True
        break """

""" if found:
    print("We have milk on the list.")
else:
    print("We do not have milk on the list.") """


""" print(shopping_list) """

#sort()
""" shopping_list.sort(reverse=True)

print(shopping_list) """

#reverse()


""" print(shopping_list)
shopping_list.reverse()
print(shopping_list) """

#random

shopping_list = ["cheese", "apples", "bread", "cheese", "milk", "eggs", "cheese"]

random_item = random.choice(shopping_list)
print(random_item)



""" for item in shopping_list:
    print(item) """