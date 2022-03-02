import mymodule as mm

path = "IndianFoodDatasetxls.xlsx"
contents = mm.read_xlsx(path)

for i in range(10):
    print(contents[i])
