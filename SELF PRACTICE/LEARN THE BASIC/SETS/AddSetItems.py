#Add Items
#To add one item to a set use the add() method.

gamesName = {"CODM", "Free Fire", "Clash of Clans"}
print("The set named gamesName contains the following games:")
for x in gamesName:
    print(x)
gamesName.add("Clash Royale")
print("Successfully added Clash Royale to the set gamesName")
for x in gamesName:
    print(x)

#To add items from another set into the current set, use the update() method.
newGames = {"Delta Force", "Valorant", "Apex Legends"}
gamesName.update(newGames)
print("Successfully added the items from the set newGames to the set gamesName")
for x in gamesName:
    print(x)    