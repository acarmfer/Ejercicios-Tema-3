# Lista de personajes de Marvel Cinematic Universe (MCU) con su año de primera aparición
marvel_characters = [
    {"name": "Iron Man", "first_appearance_year": 2008},
    {"name": "Captain America", "first_appearance_year": 2011},
    {"name": "Thor", "first_appearance_year": 2011},
    {"name": "Hulk", "first_appearance_year": 2008},
    {"name": "Black Widow", "first_appearance_year": 2010},
    {"name": "Hawkeye", "first_appearance_year": 2011},
    {"name": "Spider-Man", "first_appearance_year": 2016},
    {"name": "Black Panther", "first_appearance_year": 2016},
    {"name": "Doctor Strange", "first_appearance_year": 2016},
    {"name": "Captain Marvel", "first_appearance_year": 2019},
    {"name": "Ant-Man", "first_appearance_year": 2015},
    {"name": "Falcon", "first_appearance_year": 2014},
    {"name": "Winter Soldier", "first_appearance_year": 2011},
    {"name": "Scarlet Witch", "first_appearance_year": 2015},
    {"name": "Vision", "first_appearance_year": 2015},
    {"name": "Rocket Raccoon", "first_appearance_year": 2014},
    {"name": "Groot", "first_appearance_year": 2014},
    {"name": "Gamora", "first_appearance_year": 2014},
    {"name": "Drax the Destroyer", "first_appearance_year": 2014},
    {"name": "Star-Lord", "first_appearance_year": 2014},
]

# Función para realizar un listado ascendente de los personajes ordenados por su nombre
def sort_characters_by_name(characters):
    return sorted(characters, key=lambda x: x["name"])

# Función para indicar el primer y último personaje en aparecer en una película
def first_and_last_characters_appearance(characters):
    first_character = min(characters, key=lambda x: x["first_appearance_year"])
    last_character = max(characters, key=lambda x: x["first_appearance_year"])
    return first_character, last_character

# Función para realizar un listado de los personajes ordenados de manera descendente por año de aparición
def sort_characters_by_year_descending(characters):
    return sorted(characters, key=lambda x: x["first_appearance_year"], reverse=True)

# Función para calcular el rango de años entre el primer y el último personaje en aparecer
def calculate_year_range(characters):
    first_character, last_character = first_and_last_characters_appearance(characters)
    year_range = last_character["first_appearance_year"] - first_character["first_appearance_year"]
    return year_range

# Función para determinar si los personajes Capitan America y Rocket Raccoon están en la lista y en qué año aparecieron
def find_characters_year(characters, character_names):
    result = {}
    for name in character_names:
        for character in characters:
            if character["name"] == name:
                result[name] = character["first_appearance_year"]
                break
        else:
            result[name] = None
    return result

# Ejecutar las funciones y mostrar los resultados
sorted_characters_by_name = sort_characters_by_name(marvel_characters)
print("Listado ascendente de los personajes ordenados por nombre:")
for character in sorted_characters_by_name:
    print(character["name"])

first_character, last_character = first_and_last_characters_appearance(marvel_characters)
print("\nPrimer personaje en aparecer en una película:", first_character["name"], "(", first_character["first_appearance_year"], ")")
print("Último personaje en aparecer en una película:", last_character["name"], "(", last_character["first_appearance_year"], ")")

sorted_characters_by_year_descending = sort_characters_by_year_descending(marvel_characters)
print("\nListado de los personajes ordenados de manera descendente por año de aparición:")
for character in sorted_characters_by_year_descending:
    print(character["name"], "(", character["first_appearance_year"], ")")

year_range = calculate_year_range(marvel_characters)
print("\nRango de años entre el primer y el último personaje en aparecer:", year_range)

characters_to_find = ["Captain America", "Rocket Raccoon"]
characters_years = find_characters_year(marvel_characters, characters_to_find)
print("\nAño de aparición de los personajes:")
for character, year in characters_years.items():
    if year is not None:
        print(character, "(", year, ")")
    else:
        print(character, "no está en la lista.")


