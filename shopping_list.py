# define the dictionary
shopping_list = {
    "iSpot": ["laptop", "keyboard", "mouse"],
    "Empik": ["books", "notebooks", "pencils"]
}

# using for loop we iterate through the dictionary
# store and products names should be capitalized
for store, product in shopping_list.items():
    print(f"I'll go to {store.title()} and buy there following products: {str(product).title()}.")