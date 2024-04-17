# Lista de series de Netflix con nombre, cantidad de temporadas y cantidad de capítulos totales
netflix_series = [
    {"nombre": "Stranger Things", "temporadas": 4, "capitulos_totales": 34},
    {"nombre": "The Crown", "temporadas": 4, "capitulos_totales": 40},
    {"nombre": "Breaking Bad", "temporadas": 5, "capitulos_totales": 62},
    {"nombre": "Narcos", "temporadas": 3, "capitulos_totales": 30},
    {"nombre": "The Witcher", "temporadas": 2, "capitulos_totales": 16},
    {"nombre": "Money Heist", "temporadas": 5, "capitulos_totales": 55},
    {"nombre": "Dark", "temporadas": 3, "capitulos_totales": 26},
    {"nombre": "Stranger Things", "temporadas": 4, "capitulos_totales": 34},
    {"nombre": "The Mandalorian", "temporadas": 2, "capitulos_totales": 16},
    {"nombre": "Star Wars: Rebels", "temporadas": 4, "capitulos_totales": 75},
    {"nombre": "Los 100", "temporadas": 7, "capitulos_totales": 100},
    {"nombre": "Peaky Blinders", "temporadas": 5, "capitulos_totales": 30},
    {"nombre": "Friends", "temporadas": 10, "capitulos_totales": 236},
]

# Función para listar las series ordenadas según criterios dados
def sort_series(netflix_series, criterion):
    return sorted(netflix_series, key=lambda x: x[criterion])

# Función para mostrar toda la información de una serie específica
def find_series(netflix_series, name):
    for series in netflix_series:
        if series["nombre"] == name:
            return series
    return None

# Función para determinar la serie con mayor cantidad de temporadas y mayor cantidad de capítulos
def most_seasons_and_episodes(netflix_series):
    max_seasons_series = max(netflix_series, key=lambda x: x["temporadas"])
    max_episodes_series = max(netflix_series, key=lambda x: x["capitulos_totales"])
    return max_seasons_series, max_episodes_series

# Función para calcular la cantidad de series y el promedio de temporadas
def calculate_series_count_and_average_seasons(netflix_series):
    series_count = len(netflix_series)
    total_seasons = sum(series["temporadas"] for series in netflix_series)
    average_seasons = total_seasons / series_count
    return series_count, average_seasons

# Función para calcular el promedio de capítulos por temporada de una serie específica
def average_episodes_per_season(netflix_series, name):
    series = find_series(netflix_series, name)
    if series:
        return series["capitulos_totales"] / series["temporadas"]
    else:
        return None

# Función para listar el TOP 5 de series con mayor cantidad de capítulos
def top_5_series_by_episodes(netflix_series):
    return sorted(netflix_series, key=lambda x: x["capitulos_totales"], reverse=True)[:5]

# Función para listar el TOP 10 de series con mayor cantidad de temporadas
def top_10_series_by_seasons(netflix_series):
    return sorted(netflix_series, key=lambda x: x["temporadas"], reverse=True)[:10]

# Función para mostrar todas las series con tres o menos temporadas
def series_with_few_seasons(netflix_series):
    return [series for series in netflix_series if series["temporadas"] <= 3]

# Ejecutar las funciones y mostrar los resultados
print("Listado de series ordenadas por nombre:")
for series in sort_series(netflix_series, "nombre"):
    print(series)

print("\nInformación de la serie 'Los 100':")
print(find_series(netflix_series, "Los 100"))

max_seasons_series, max_episodes_series = most_seasons_and_episodes(netflix_series)
print("\nSerie con mayor cantidad de temporadas:", max_seasons_series)
print("Serie con mayor cantidad de capítulos:", max_episodes_series)

series_count, average_seasons = calculate_series_count_and_average_seasons(netflix_series)
print("\nCantidad de series en la plataforma:", series_count)
print("Promedio de temporadas por serie:", average_seasons)

print("\nPromedio de capítulos por temporada de la serie 'Star Wars: Rebels':")
print(average_episodes_per_season(netflix_series, "Star Wars: Rebels"))

print("\nTOP 5 de series con mayor cantidad de capítulos:")
for series in top_5_series_by_episodes(netflix_series):
    print(series)

print("\nTOP 10 de series con mayor cantidad de temporadas:")
for series in top_10_series_by_seasons(netflix_series):
    print(series)

print("\nSeries con tres o menos temporadas:")
for series in series_with_few_seasons(netflix_series):
    print(series)
