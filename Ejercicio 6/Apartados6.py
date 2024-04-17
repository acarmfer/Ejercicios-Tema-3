# Lista de caballeros Jedi y lores Sith con nombre y maestro
jedi_and_sith = [
    {"nombre": "Obi-Wan Kenobi", "maestro": "Qui-Gon Jinn"},
    {"nombre": "Anakin Skywalker", "maestro": "Obi-Wan Kenobi"},
    {"nombre": "Yoda", "maestro": None},
    {"nombre": "Qui-Gon Jinn", "maestro": None},
    {"nombre": "Mace Windu", "maestro": "Yoda"},
    {"nombre": "Darth Sidious", "maestro": None},
    {"nombre": "Darth Vader", "maestro": "Darth Sidious"},
    {"nombre": "Count Dooku", "maestro": "Darth Sidious"},
    {"nombre": "Darth Maul", "maestro": "Darth Sidious"},
    {"nombre": "Darth Malak", "maestro": "Darth Revan"},
    {"nombre": "Darth Revan", "maestro": None}
]

# Función para realizar un listado ordenado por nombre
def sort_characters_by_name(characters):
    return sorted(characters, key=lambda x: x["nombre"])

# Función para listar todos los Jedi ordenados por nombre
def filter_jedi(characters):
    return [character for character in characters if character["maestro"] is not None]

# Función para listar todos los Sith ordenados por nombre
def filter_sith(characters):
    return [character for character in characters if character["maestro"] is None]

# Función para mostrar los aprendices de un maestro dado y contar cuántos aprendices tuvo
def apprentices_of_master(characters, master_name):
    apprentices = [character for character in characters if character["maestro"] == master_name]
    return apprentices, len(apprentices)

# Función para determinar si un personaje está en la lista y mostrar su información
def find_character(characters, name):
    for character in characters:
        if character["nombre"] == name:
            return character
    return None

# Función para mostrar la posición de un personaje en la lista
def find_position(characters, name):
    for i, character in enumerate(characters):
        if character["nombre"] == name:
            return i + 1
    return None

# Ejecutar las funciones y mostrar los resultados
sorted_characters = sort_characters_by_name(jedi_and_sith)
print("Listado ordenado por nombre:")
for character in sorted_characters:
    print(character)

jedi = filter_jedi(jedi_and_sith)
print("\nListado de todos los Jedi ordenados por nombre:")
for character in jedi:
    print(character["nombre"])

sith = filter_sith(jedi_and_sith)
print("\nListado de todos los Sith ordenados por nombre:")
for character in sith:
    print(character["nombre"])

palpatine_apprentices, palpatine_apprentices_count = apprentices_of_master(jedi_and_sith, "Darth Sidious")
print(f"\nAprendices de Palpatine ({palpatine_apprentices_count}):")
for apprentice in palpatine_apprentices:
    print(apprentice["nombre"])

obi_wan_apprentices, obi_wan_apprentices_count = apprentices_of_master(jedi_and_sith, "Obi-Wan Kenobi")
print(f"\nAprendices de Obi-Wan Kenobi ({obi_wan_apprentices_count}):")
for apprentice in obi_wan_apprentices:
    print(apprentice["nombre"])

dath_malak_info = find_character(jedi_and_sith, "Darth Malak")
if dath_malak_info:
    print("\nInformación de Dath Malak:", dath_malak_info)
else:
    print("\nDath Malak no está en la lista.")

yoda_position = find_position(sorted_characters, "Yoda")
if yoda_position:
    print("\nYoda se encuentra en la posición:", yoda_position)
else:
    print("\nYoda no está en la lista.")
