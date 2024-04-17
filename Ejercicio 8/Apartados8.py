# Lista de películas con título, año de estreno, recaudación y valoración del público
movies = [
    {"titulo": "Iron Man", "año": 2008, "recaudacion": 585, "valoracion": 4},
    {"titulo": "Avengers: Infinity War", "año": 2018, "recaudacion": 2048, "valoracion": 5},
    {"titulo": "Star Wars: The Return of the Jedi", "año": 1983, "recaudacion": 572.7, "valoracion": 4.5},
    {"titulo": "Iron Man 2", "año": 2010, "recaudacion": 623.9, "valoracion": 4},
    {"titulo": "Avengers: Endgame", "año": 2019, "recaudacion": 2797, "valoracion": 4.8},
    {"titulo": "Iron Man 3", "año": 2013, "recaudacion": 1214, "valoracion": 4},
    {"titulo": "Captain America: Civil War", "año": 2016, "recaudacion": 1153, "valoracion": 4.5},
    {"titulo": "The Avengers", "año": 2012, "recaudacion": 1519, "valoracion": 4.5},
    {"titulo": "Thor: Ragnarok", "año": 2017, "recaudacion": 854, "valoracion": 4.2},
    {"titulo": "Black Panther", "año": 2018, "recaudacion": 1347, "valoracion": 4.3}
]

# Función para realizar un listado ordenado por título, año de lanzamiento y por recaudación (descendente)
def sort_movies(movies):
    return sorted(movies, key=lambda x: (x["titulo"], x["año"], x["recaudacion"]), reverse=True)

# Función para mostrar toda la información de la película que más recaudó
def most_successful_movie(movies):
    return max(movies, key=lambda x: x["recaudacion"])

# Función para listar todas las películas que tengan valoración 5
def top_rated_movies(movies):
    return [movie for movie in movies if movie["valoracion"] == 5]

# Función para determinar si una película está en la lista y mostrar toda su información
def find_movie_by_title(movies, title):
    for movie in movies:
        if movie["titulo"] == title:
            return movie
    return None

# Función para indicar en qué posición se encuentra una película
def find_movie_position(movies, title):
    for i, movie in enumerate(movies, start=1):
        if movie["titulo"] == title:
            return i
    return None

# Función para calcular el total recaudado por las películas que incluyen la palabra "Avengers" en su título
def total_revenue_avengers(movies):
    avengers_movies = [movie for movie in movies if "Avengers" in movie["titulo"]]
    return sum(movie["recaudacion"] for movie in avengers_movies)

# Función para mostrar todas las películas que se estrenaron en un año específico
def movies_by_year(movies, year):
    return [movie for movie in movies if movie["año"] == year]

# Función para listar todas las películas que comienzan con una palabra específica
def movies_starting_with_word(movies, word):
    return [movie for movie in movies if movie["titulo"].startswith(word)]

# Ejecutar las funciones y mostrar los resultados
sorted_movies = sort_movies(movies)
print("Listado ordenado por título, año de lanzamiento y por recaudación (descendente):")
for movie in sorted_movies:
    print(movie)

most_successful = most_successful_movie(movies)
print("\nInformación de la película que más recaudó:")
print(most_successful)

top_rated = top_rated_movies(movies)
print("\nListado de todas las películas con valoración 5:")
for movie in top_rated:
    print(movie)

avengers_infinity_war_info = find_movie_by_title(movies, "Avengers: Infinity War")
if avengers_infinity_war_info:
    print("\nInformación de la película 'Avengers: Infinity War':")
    print(avengers_infinity_war_info)
else:
    print("\nLa película 'Avengers: Infinity War' no está en la lista.")

star_wars_return_of_jedi_position = find_movie_position(sorted_movies, "Star Wars: The Return of the Jedi")
print("\nPosición de la película 'Star Wars: The Return of the Jedi':", star_wars_return_of_jedi_position)

total_revenue_avengers_movies = total_revenue_avengers(movies)
print("\nTotal recaudado por las películas que incluyen la palabra 'Avengers':", total_revenue_avengers_movies)

movies_2017 = movies_by_year(movies, 2017)
print("\nListado de todas las películas estrenadas en el año 2017:")
for movie in movies_2017:
    print(movie)

iron_movies = movies_starting_with_word(movies, "Iron")
print("\nListado de todas las películas que comienzan con la palabra 'Iron':")
for movie in iron_movies:
    print(movie)
