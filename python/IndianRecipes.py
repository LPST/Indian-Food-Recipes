import mymodule as mm

def main():
    path = "IndianFoodDatasetxls.xlsx"
    contents = mm.read_xlsx(path,20)
    labels, recipes = extract_data(contents,20)

    ingredient_dict = ingredient_counts(recipes)
    high_ten = ('',0)
    for key in ingredient_dict.keys():
        for num in high_ten:
            if high_ten(1) < ingredident_dict[key]:
                high_ten = (key, ingredient_dict[key])
    print(high_ten)

def extract_data(contents, num_rows=None):
    labels = contents[0]
    recipes = []
    if type(num_rows) == int:
        last_row = num_rows
    else:
        last_row = len(contents)
    for i in range(1, last_row):
        uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url = contents[i]
        recipe = Recipe(uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url)
        recipes.append(recipe)
    return labels, recipes

class Recipe:
    def __init__(self, uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url):
        self.uid = uid
        self.name_h = str(name_h)
        self.name_e = str(name_e)
        self.ingredients_h = str(ingredients_h)
        self.ingredients_e = str(ingredients_e)
        self.prep = int(prep)
        self.cook = int(cook)
        self.total = int(total)
        self.servings = int(servings)
        self.cuisine = str(cuisine)
        self.course = str(course)
        self.diet = str(diet)
        self.instructions_h = str(instructions_h)
        self.instructions_e = str(instructions_e)
        self.url = str(url)

    def __repr__(self):
        return "<Recipe uid:%s \nname_h:%s \nname_e:%s \ningredients_h:%s \ningredients_e:%s \nprep:%i \ncook:%i \ntotal:%i \nservings:%i \ncuisine:%s \ncourse:%s \ndiet:%s instructions_h:%s, \ninstructions_e:%s \nurl:%s>" % (self.uid, self.name_h, self.name_e, self.ingredients_h, self.ingredients_e, self.prep, self.cook, self.total, self.servings, self.cuisine, self.course, self.diet, self.instructions_h, self.instructions_e, self.url)
    def search_attr(self, attr, value):

        if type(getattr(self, attr)) != str:
            print("Sorry, search_attr literally can't handle non-string attributes right now.")
            return None
        elif getattr(self, attr).casefold().find(value) >= 0:
            return True
        else:
            return False

def search_recipes(recipes, attr, value):
    results = []
    for i in range(len(recipes)):
        search_bool = recipes[i].search_attr(attr, value)
        if search_bool == False:
            pass
        else:
            results.append(recipes[i])
    return results

def ingredient_counts(recipes):
    #this will not distinguish between "2 cups butter" and "3 cups butter" because those strings are not identical. I think I need to use regex to get the word after the number and before the hyphen
    counts = {}
    for i in range(len(recipes)):
        for ingredient in getattr(recipes[i], "ingredients_e").split(","):
            if ingredient in counts.keys():
                counts.update((ingredient, counts[ingredient] + 1))
            else:
                counts[ingredient] = 1
    return counts
if __name__ == '__main__':
    main()
