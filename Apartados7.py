# Lista de dioses griegos
gods = [
    "Zeus", "Poseidón", "Hades", "Hera", "Atenea", "Apolo", "Artemisa", "Hermes", "Ares", "Hefesto", "Deméter",
    "Afrodita", "Hestia", "Dionisio", "Heracles", "Perseo", "Helena", "Héctor", "Hermione"
]

# Función para emitir un listado de todos los dioses ordenados
def sort_gods(gods):
    return sorted(gods)

# Función para determinar si Atenea está en la lista
def find_atenea(gods):
    return "Atenea" in gods

# Función para indicar en qué posición se encuentra Deméter
def find_demeter_position(gods):
    return gods.index("Deméter") + 1 if "Deméter" in gods else None

# Función para listar todos los dioses que comienzan con la letra H y determinar cuántos son
def filter_gods_by_letter(gods, letter):
    filtered_gods = [god for god in gods if god.startswith(letter)]
    return filtered_gods, len(filtered_gods)

# Función para agregar al dios Helios y volver a listar los dioses ordenados alfabéticamente
def add_helios(gods):
    gods.append("Helios")
    return sort_gods(gods)

# Ejecutar las funciones y mostrar los resultados
sorted_gods = sort_gods(gods)
print("Listado de todos los dioses ordenados:")
for god in sorted_gods:
    print(god)

if find_atenea(gods):
    print("\nAtenea está en la lista.")
else:
    print("\nAtenea no está en la lista.")

demeter_position = find_demeter_position(gods)
if demeter_position:
    print("\nDeméter se encuentra en la posición:", demeter_position)
else:
    print("\nDeméter no está en la lista.")

h_gods, h_gods_count = filter_gods_by_letter(gods, "H")
print("\nListado de todos los dioses que comienzan con la letra H:")
for god in h_gods:
    print(god)
print("Cantidad de dioses que comienzan con la letra H:", h_gods_count)

gods_with_helios = add_helios(gods)
print("\nListado de todos los dioses ordenados con Helios añadido:")
for god in gods_with_helios:
    print(god)
