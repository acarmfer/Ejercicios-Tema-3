# Lista de personajes de Star Wars
star_wars_characters = [
    "Darth Vader", "Luke Skywalker", "Princess Leia", "Han Solo", "Obi-Wan Kenobi",
    "Yoda", "Chewbacca", "R2-D2", "C-3PO", "Darth Maul", "Hera Syndulla", "Lando Calrissian"
]

# Función para ordenar alfabéticamente los personajes de Star Wars
def sort_characters(characters):
    return sorted(characters)

# Función para determinar si Darth Maul está en la lista y en qué posición se encuentra
def find_darth_maul(characters):
    if "Darth Maul" in characters:
        return characters.index("Darth Maul") + 1
    else:
        return None

# Función para mostrar información de personajes antes y después de Hera Syndulla
def get_characters_around_hera(characters):
    index_hera = characters.index("Hera Syndulla")
    before_hera = characters[:index_hera]
    after_hera = characters[index_hera + 1:]
    return before_hera, after_hera

# Función para listar personajes que comienzan con la letra "L"
def filter_characters_by_letter(characters, letter):
    return [char for char in characters if char.startswith(letter)]

# Ordenar alfabéticamente los personajes
sorted_characters = sort_characters(star_wars_characters)
print("Personajes ordenados alfabéticamente:", sorted_characters)

# Determinar si Darth Maul está en la lista y en qué posición se encuentra
position_darth_maul = find_darth_maul(star_wars_characters)
if position_darth_maul is not None:
    print("Darth Maul está en la posición:", position_darth_maul)
else:
    print("Darth Maul no está en la lista.")

# Mostrar información de personajes antes y después de Hera Syndulla
before_hera, after_hera = get_characters_around_hera(sorted_characters)
print("Personajes antes de Hera Syndulla:", before_hera)
print("Personajes después de Hera Syndulla:", after_hera)

# Listar personajes que comienzan con la letra "L"
characters_starting_with_L = filter_characters_by_letter(star_wars_characters, "L")
print("Personajes que comienzan con la letra 'L':", characters_starting_with_L)
