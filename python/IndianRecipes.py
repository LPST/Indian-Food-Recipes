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
    """
    a function to convert the string entries of the excel file to recipe objects

    """
    #num_rows is their for convenience. When testing a function, we don't need to load all 6000 rows. 
    labels = contents[0]
    recipes = []
    if type(num_rows) == int: 
        last_row = num_rows
    else:
        last_row = len(contents)
    for i in range(1, last_row): #loop through the rows, create a Recipe object, and add it to the list
        uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url = contents[i]
        recipe = Recipe(uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url)
        recipes.append(recipe)
    return labels, recipes

class Recipe:
    def __init__(self, uid, name_h, name_e, ingredients_h, ingredients_e, prep, cook, total, servings, cuisine, course, diet, instructions_h, instructions_e, url):
        #copy and paste the values, make sure they are the right types
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
        #the internet told me this is a standard format for a __repr__ string
        return "<Recipe uid:%s \nname_h:%s \nname_e:%s \ningredients_h:%s \ningredients_e:%s \nprep:%i \ncook:%i \ntotal:%i \nservings:%i \ncuisine:%s \ncourse:%s \ndiet:%s instructions_h:%s, \ninstructions_e:%s \nurl:%s>" % (self.uid, self.name_h, self.name_e, self.ingredients_h, self.ingredients_e, self.prep, self.cook, self.total, self.servings, self.cuisine, self.course, self.diet, self.instructions_h, self.instructions_e, self.url)

    def search_attr(self, attr, value):
        """
        This function searches the object's attribute for a given value 
        """
        if type(getattr(self, attr)) != str:#some basic error handling in case someone searches by prep time
            print("Sorry, search_attr literally can't handle non-string attributes right now.")
            return None
        elif getattr(self, attr).casefold().find(value.casefold()) >= 0: #this will be -1 if the find() function doesn't
            return True
        else:
            return False

def search_recipes(recipes, attr, value):
    results = []
    for i in range(len(recipes)): #for each recipe
        search_bool = recipes[i].search_attr(attr, value) #search the recipe for the specified value
        if search_bool == False:
            pass
        else:
            results.append(recipes[i]) #if it's in the recipe, add it to the output
    return results

def attr_counts(recipes, attr):
    #this will not distinguish between "2 cups butter" and "3 cups butter" because those strings are not identical. I think I need to use regex to get the word after the number and before the hyphen
    counts = {}
    for i in range(len(recipes)): #for each recipe
        for ingredient in getattr(recipes[i], attr).split(","): #for each ingredient in the recipes' list of ingredients
            if ingredient in counts.keys(): #if the ingredient is in the count already
                counts.update({ingredient:counts[ingredient] + 1})#increment the count
            else:
                counts.update({ingredient:1}) #if it's not in the count, add it to the count
    return counts

def highest_attr_counts(recipes, attr, n):
    attr_dict = attr_counts(recipes, attr) #get the counts
    highest_n = [['',0]]*n #preload the results
    for key in attr_dict.keys(): #for each ingredient in the count
        for i in range(len(highest_n)): #check each element of the results
            if highest_n[i][1] < attr_dict[key]: #if its count is higher than any of the results
                highest_n[i] = [key, attr_dict[key]] #add it to the results
                break
    return highest_n 
if __name__ == '__main__':
    main()
