# Lista de Funko Pop con número, nombre, colección y precio
funko_pop_list = [
    {"numero": 130, "nombre": "Darth Vader", "coleccion": "Star Wars", "precio": 15.99},
    {"numero": 295, "nombre": "Iron Man", "coleccion": "Marvel", "precio": 12.99},
    {"numero": 512, "nombre": "Capitana Marvel", "coleccion": "Marvel", "precio": 14.99},
    {"numero": 728, "nombre": "Red Skull", "coleccion": "Marvel", "precio": 11.99},
    {"numero": 820, "nombre": "Thanos", "coleccion": "Marvel", "precio": 17.99},
    {"numero": 934, "nombre": "Galactus", "coleccion": "Marvel", "precio": 19.99},
    {"numero": 1056, "nombre": "Harry Potter", "coleccion": "Harry Potter", "precio": 16.99},
    {"numero": 1152, "nombre": "Tony Stark", "coleccion": "Marvel", "precio": 13.99},
    {"numero": 1235, "nombre": "Dumbledore", "coleccion": "Harry Potter", "precio": 18.99},
    {"numero": 1314, "nombre": "Ron Weasley", "coleccion": "Harry Potter", "precio": 15.99},
]

# Función para realizar un listado ordenado por número
def sort_funko_pop_by_number(funko_pop_list):
    return sorted(funko_pop_list, key=lambda x: x["numero"])

# Función para realizar un listado de los Funko Pop de una colección
def filter_funko_pop_by_collection(funko_pop_list, collection):
    return [funko for funko in funko_pop_list if funko["coleccion"] == collection]

# Función para determinar si tiene disponible un Funko Pop específico de una colección y mostrar toda la información
def find_funko_pop(funko_pop_list, number, collection):
    for funko in funko_pop_list:
        if funko["numero"] == number and funko["coleccion"] == collection:
            return funko
    return None

# Función para mostrar todos los Funko Pop disponibles con un número específico
def show_funko_pop_by_number(funko_pop_list, number):
    return [funko for funko in funko_pop_list if funko["numero"] == number]

# Función para listar todos los modelos de un personaje específico
def filter_funko_pop_by_name(funko_pop_list, name):
    return [funko for funko in funko_pop_list if funko["nombre"] == name]

# Función para calcular el costo de todos los modelos de un personaje específico
def calculate_cost_by_name(funko_pop_list, name):
    return sum(funko["precio"] for funko in funko_pop_list if funko["nombre"] == name)

# Función para determinar si existen Funko Pop de ciertos personajes y mostrar su información
def find_funko_pop_by_names(funko_pop_list, names):
    result = {}
    for name in names:
        found = [funko for funko in funko_pop_list if funko["nombre"] == name]
        if found:
            result[name] = found
    return result

# Función para calcular el promedio de costo de todos los Funko Pop y el costo total de las colecciones
def calculate_average_and_total_cost(funko_pop_list):
    total_cost = sum(funko["precio"] for funko in funko_pop_list)
    average_cost = total_cost / len(funko_pop_list)
    
    rocks_cost = sum(funko["precio"] for funko in funko_pop_list if funko["coleccion"] == "Rocks")
    harry_potter_cost = sum(funko["precio"] for funko in funko_pop_list if funko["coleccion"] == "Harry Potter")
    
    return average_cost, rocks_cost + harry_potter_cost

# Ejecutar las funciones y mostrar los resultados
sorted_funko_pop_by_number = sort_funko_pop_by_number(funko_pop_list)
print("Listado de Funko Pop ordenados por número:")
for funko in sorted_funko_pop_by_number:
    print(funko)

marvel_funko_pop = filter_funko_pop_by_collection(funko_pop_list, "Marvel")
print("\nListado de Funko Pop de la colección Marvel:")
for funko in marvel_funko_pop:
    print(funko)

funko_130_star_wars = find_funko_pop(funko_pop_list, 130, "Star Wars")
if funko_130_star_wars:
    print("\nInformación del Funko Pop 130 de la colección Star Wars:", funko_130_star_wars)
else:
    print("\nEl Funko Pop 130 de la colección Star Wars no está disponible.")

funko_295_info = show_funko_pop_by_number(funko_pop_list, 295)
if funko_295_info:
    print("\nInformación de todos los Funko Pop disponibles con número 295:")
    for funko in funko_295_info:
        print(funko)
else:
    print("\nNo hay Funko Pop disponibles con número 295.")

darth_vader_models = filter_funko_pop_by_name(funko_pop_list, "Darth Vader")
print("\nModelos de Funko Pop de Darth Vader:")
for funko in darth_vader_models:
    print(funko)

capitana_marvel_models = filter_funko_pop_by_name(funko_pop_list, "Capitana Marvel")
print("\nModelos de Funko Pop de Capitana Marvel:")
for funko in capitana_marvel_models:
    print(funko)

names_to_find = ["Red Skull", "Thanos", "Galactus"]
found_funko_pop = find_funko_pop_by_names(funko_pop_list, names_to_find)
print("\nFunko Pop encontrados:")
for name, funko_pop in found_funko_pop.items():
    print(f"Nombre: {name}")
    for funko in funko_pop:
        print(f"Funko: {funko}")

tony_stark_cost = calculate_cost_by_name(funko_pop_list, "Tony Stark")
iron_man_cost = calculate_cost_by_name(funko_pop_list, "Iron Man")
print("\nCosto de todos los modelos de Tony Stark:", tony_stark_cost)
print("Costo de todos los modelos de Iron Man:", iron_man_cost)

average_cost, total_collections_cost = calculate_average_and_total_cost(funko_pop_list)
print("\nPromedio de costo de todos los Funko Pop:", average_cost)
print("Costo total de las colecciones de Rocks y Harry Potter:", total_collections_cost)

