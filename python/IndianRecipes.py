import mymodule as mm

def main():
    path = "IndianFoodDatasetxls.xlsx"
    contents = mm.read_xlsx(path)
    labels, recipes = extract_data(contents)

    a = highest_attr_counts(recipes, "ingredients_e", 3)
    b = highest_attr_counts(recipes, "cuisine", 3)
    c = highest_attr_counts(recipes, "diet", 3)
    d = highest_attr_counts(recipes, "course", 3)
    
    for x in [a,b,c,d]:
        for pair in x:
            print(pair)



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
        elif getattr(self, attr).casefold().find(value.casefold()) >= 0:
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

def attr_counts(recipes, attr):
    #this will not distinguish between "2 cups butter" and "3 cups butter" because those strings are not identical. I think I need to use regex to get the word after the number and before the hyphen
    counts = {}
    for i in range(len(recipes)):
        for ingredient in getattr(recipes[i], attr).split(","):
            if ingredient in counts.keys():
                counts.update({ingredient:counts[ingredient] + 1})
            else:
                counts.update({ingredient:1})
    return counts

def highest_attr_counts(recipes, attr, n):
    attr_dict = attr_counts(recipes, attr)
    highest_n = [['',0]]*n
    for key in attr_dict.keys():
        for i in range(len(highest_n)):
            if highest_n[i][1] < attr_dict[key]:
                highest_n[i] = [key, attr_dict[key]]
                break
    return highest_n
if __name__ == '__main__':
    main()
