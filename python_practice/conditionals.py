# if else example
disney_movies = ["Mulan", "Hercules", "Pocahontas", "Aladdin"]
for movie in disney_movies:
    if movie == "Pocahontas":
        print(f"{movie} is bad")
    else:
        print(f"{movie} is good")
print()

# in keyword
print("Hercules" in disney_movies) # checks if list contains elements (don't need to loop manually)
print("Shrek" in disney_movies)

# use in keyword in conditionals
animation = "Anastasia"
if animation not in disney_movies:
    print(f"{animation} is not made by Disney")
print()

# elif branches
regions = ["North America", "Europe", "Middle East", "Africa", "Asia", "Australia"]
for i in range(0, len(regions)):
    price = 100
    if(i == 1):
        price = 300
    elif(i > 1 and i <= 3):
        price = 200
    elif(i == 4):
        price = 400
    elif(i == 5):
        price = 250
    print(f"{regions[i]} ticket == {price}")

# checking a list is empty
thracia_alts = []
if(thracia_alts):
    print(thracia_alts)
else:
    print("There are no Thracia Alts")