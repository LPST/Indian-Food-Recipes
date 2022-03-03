import mymodule as mm

def main():
    path = "IndianFoodDatasetxls.xlsx"
    contents = mm.read_xlsx(path, 28)
    labels, recipes = extract_data(contents, 28)
    print (recipes[24])

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
        self.name_h = name_h
        self.name_e = name_e
        self.ingredients_h = str(ingredients_h).split(",")
        self.ingredients_e = str(ingredients_e).split(",")
        self.prep = int(prep)
        self.cook = int(cook)
        self.total = int(total)
        self.servings = int(servings)
        self.cuisine = cuisine
        self.course = course
        self.diet = diet
        self.instructions_h = instructions_h
        self.instructions_e = instructions_e
        self.url = url

    def __repr__(self):
        return "<Recipe uid:%s \nname_h:%s \nname_e:%s \ningredients_h:%s \ningredients_e:%s \nprep:%i \ncook:%i \ntotal:%i \nservings:%i \ncuisine:%s \ncourse:%s \ndiet:%s instructions_h:%s, \ninstructions_e:%s \nurl:%s>" % (self.uid, self.name_h, self.name_e, str(self.ingredients_h), str(self.ingredients_e), self.prep, self.cook, self.total, self.servings, self.cuisine, self.course, self.diet, self.instructions_h, self.instructions_e, self.url)
if __name__ == '__main__':
    main()
