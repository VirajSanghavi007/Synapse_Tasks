from itertools import combinations

Pokedex = {
"Pikachu": ("Electric",),
"‘Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}

k = int(input("Enter the number of members in a Team: "))
max_types = 0
list1 = []
list2 = []
types = set()
pokemon = set()

for i in combinations(Pokedex, k):
    for j in i:
        types.update(Pokedex[j])
        pokemon.add(j)
    if max < len(types):
        max = len(types)
        list1 = [i for i in types]
        list2 = [i for i in pokemon]
    types.clear()
    pokemon.clear()
    
print("The strongest team is ", list2)
print(f"The total number of types this team has is {list1} which has {max} unique types.")

