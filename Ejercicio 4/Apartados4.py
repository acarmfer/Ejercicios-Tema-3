# Lista de Pokémon con nombre, número y tipo principal
pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "Planta"},
    {"nombre": "Charmander", "numero": 4, "tipo": "Fuego"},
    {"nombre": "Squirtle", "numero": 7, "tipo": "Agua"},
    {"nombre": "Pikachu", "numero": 25, "tipo": "Eléctrico"},
    {"nombre": "Jigglypuff", "numero": 39, "tipo": "Normal"},
    {"nombre": "Mewtwo", "numero": 150, "tipo": "Psíquico"},
    {"nombre": "Mew", "numero": 151, "tipo": "Psíquico"},
    {"nombre": "Typhlosion", "numero": 157, "tipo": "Fuego"},
    {"nombre": "Totodile", "numero": 158, "tipo": "Agua"},
    {"nombre": "Entei", "numero": 244, "tipo": "Fuego"},
    {"nombre": "Raikou", "numero": 243, "tipo": "Eléctrico"},
    {"nombre": "Suicune", "numero": 245, "tipo": "Agua"},
    {"nombre": "Cobalion", "numero": 638, "tipo": "Acero"},
    {"nombre": "Terrakion", "numero": 639, "tipo": "Roca"},
    {"nombre": "Virizion", "numero": 640, "tipo": "Planta"},
]

# Función para ordenar los Pokémon por número usando el método de ordenamiento por conteo
def count_sort_pokemon(pokemons):
    max_number = max(pokemons, key=lambda x: x["numero"])["numero"]
    count = [0] * (max_number + 1)
    sorted_pokemons = [None] * len(pokemons)
    for pokemon in pokemons:
        count[pokemon["numero"]] += 1
    for i in range(1, max_number + 1):
        count[i] += count[i - 1]
    for pokemon in reversed(pokemons):
        sorted_pokemons[count[pokemon["numero"]] - 1] = pokemon
        count[pokemon["numero"]] -= 1
    return sorted_pokemons

# Función para ordenar los Pokémon por nombre usando el método de ordenamiento rápido (quicksort)
def quicksort_pokemon(pokemons):
    if len(pokemons) <= 1:
        return pokemons
    pivot = pokemons[len(pokemons) // 2]
    left = [pokemon for pokemon in pokemons if pokemon["nombre"] < pivot["nombre"]]
    middle = [pokemon for pokemon in pokemons if pokemon["nombre"] == pivot["nombre"]]
    right = [pokemon for pokemon in pokemons if pokemon["nombre"] > pivot["nombre"]]
    return quicksort_pokemon(left) + middle + quicksort_pokemon(right)

# Función para mostrar toda la información de un Pokémon dado su número
def show_pokemon_info_by_number(pokemons, number):
    for pokemon in pokemons:
        if pokemon["numero"] == number:
            return pokemon
    return None

# Función para listar los Pokémon que comienzan con la letra T
def filter_pokemon_by_letter(pokemons, letter):
    return [pokemon for pokemon in pokemons if pokemon["nombre"].startswith(letter)]

# Función para determinar si existe un Pokémon dado su nombre y mostrar toda su información
def find_pokemon_by_name(pokemons, name):
    for pokemon in pokemons:
        if pokemon["nombre"] == name:
            return pokemon
    return None

# Función para listar los Pokémon de tipo eléctrico y contar cuántos son
def filter_pokemon_by_type(pokemons, type_name):
    electric_pokemons = [pokemon for pokemon in pokemons if pokemon["tipo"] == type_name]
    return electric_pokemons, len(electric_pokemons)

# Ejecutar las funciones y mostrar los resultados
sorted_pokemons_by_number = count_sort_pokemon(pokemons)
print("Listado de Pokémons ordenados por número:")
for pokemon in sorted_pokemons_by_number:
    print("Número:", pokemon["numero"], "- Nombre:", pokemon["nombre"], "- Tipo:", pokemon["tipo"])

sorted_pokemons_by_name = quicksort_pokemon(pokemons)
print("\nListado de Pokémons ordenados por nombre:")
for pokemon in sorted_pokemons_by_name:
    print("Número:", pokemon["numero"], "- Nombre:", pokemon["nombre"], "- Tipo:", pokemon["tipo"])

pokemon_640_info = show_pokemon_info_by_number(pokemons, 640)
print("\nInformación del Pokémon número 640:", pokemon_640_info)

pokemon_starting_with_T = filter_pokemon_by_letter(pokemons, "T")
print("\nListado de Pokémons que comienzan con la letra 'T':")
for pokemon in pokemon_starting_with_T:
    print("Número:", pokemon["numero"], "- Nombre:", pokemon["nombre"], "- Tipo:", pokemon["tipo"])

cobalion_info = find_pokemon_by_name(pokemons, "Cobalion")
if cobalion_info:
    print("\nInformación del Pokémon Cobalion:", cobalion_info)
else:
    print("\nEl Pokémon Cobalion no está en la lista.")

electric_pokemons, electric_pokemons_count = filter_pokemon_by_type(pokemons, "Eléctrico")
print("\nListado de Pokémons de tipo eléctrico:")
for pokemon in electric_pokemons:
    print("Número:", pokemon["numero"], "- Nombre:", pokemon["nombre"], "- Tipo:", pokemon["tipo"])
print("Cantidad de Pokémons de tipo eléctrico:", electric_pokemons_count)
