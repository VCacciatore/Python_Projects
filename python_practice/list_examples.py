# list examples

# indexing into a list
cthonics = ["Hades", "Persephone", "Zagreus", "Nyx", "Thanatos"]
print("***** LIST INDEXING *****")
print(cthonics[0])
print(cthonics[2])
print(cthonics[-1]) # negative indexing goes from the back of the list to the front
print(cthonics[-2]) # last element = -1, 2nd to last element = -2, and so on
print(cthonics)
print(f"{cthonics[2]} + {cthonics[4]}")
print("\n\n\n")

# modifying a list
olympions = ["Athena", "Dionysus", "Venus", "Demeter", "Zeus", "Hestia", "Ares", "Hermes"]
print("***** MODIYFING A LIST *****")
print(olympions)
# changing an element
olympions[2] = "Aphrodite"
print(olympions)
# adding an element
olympions.append("Apollo")
olympions.append("Hera")
print(olympions)
# inserting an element
olympions.insert(4, "Poseidon")
olympions.insert(11, "Artemis")
print(olympions)
# deleting an element
del olympions[6]
print(olympions)
# popping an object
blessing = olympions.pop()
print(olympions)
print(f"popped object = {blessing}")
# removing w/o index
olympions.append("Ares")
print(olympions)
olympions.remove("Ares") 
print(olympions) # notice how only the first instance of the word is removed

# organizing a list
print("***** ORGANIZING A LIST *****")
underworld = cthonics
# .sort() method
cthonics.sort()
print(cthonics)
print(underworld) #notice underworld is a pointer and so is cthonics
# temporarily sorting with sorted() method
print(sorted(olympions))
print(olympions)
# reverse sort
cthonics.reverse()
print(cthonics)
# len() method = .length() in JAVA
print(len(olympions))
print(len(underworld))


