# define the dictionary
shopping_list = {
    "iSpot": ["laptop", "keyboard", "mouse"],
    "Empik": ["books", "notebooks", "pencils"]
}

# using for loop we iterate through the dictionary
# store and products names should be capitalized
for store, product in shopping_list.items():
    print(f"I'll go to {store.title()} and buy there following products: {str(product).title()}.")

# using list comprehension we calculate the amount of purchased products
amount_products = sum([len(product) for product in shopping_list.values()])
print(f"I'll buy {amount_products} products in total.")