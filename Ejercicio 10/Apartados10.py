# Lista de canciones con nombre, banda o artista y año de lanzamiento del álbum
songs = [
    {"nombre": "Smells Like Teen Spirit", "banda_artista": "Nirvana", "año_lanzamiento": 1991},
    {"nombre": "Fake tales of San Francisco", "banda_artista": "Arctic Monkeys", "año_lanzamiento": 2006},
    {"nombre": "Black hole sun", "banda_artista": "Soundgarden", "año_lanzamiento": 1994},
    {"nombre": "Under the Bridge", "banda_artista": "Red Hot Chili Peppers", "año_lanzamiento": 1991},
    {"nombre": "Cochise", "banda_artista": "Audioslave", "año_lanzamiento": 2002},
    {"nombre": "Paint it Black", "banda_artista": "The Rolling Stones", "año_lanzamiento": 1966},
    {"nombre": "Californication", "banda_artista": "Red Hot Chili Peppers", "año_lanzamiento": 1999},
    {"nombre": "Bohemian Rhapsody", "banda_artista": "Queen", "año_lanzamiento": 1975},
    {"nombre": "Bittersweet Symphony", "banda_artista": "The Verve", "año_lanzamiento": 1997},
]

# Función para realizar un listado ordenado por diferentes criterios
def sort_songs(songs, criterion):
    if criterion == "cancion":
        return sorted(songs, key=lambda x: x["nombre"])
    elif criterion == "banda_artista":
        return sorted(songs, key=lambda x: x["banda_artista"])
    elif criterion == "año_lanzamiento":
        return sorted(songs, key=lambda x: x["año_lanzamiento"])

# Función para determinar si existe alguna canción de una banda o artista específico
def find_songs_by_artist(songs, artist):
    return any(song["banda_artista"] == artist for song in songs)

# Función para mostrar todas las canciones de una banda o artista específico
def songs_by_artist(songs, artist):
    return [song for song in songs if song["banda_artista"] == artist]

# Función para agregar una nueva canción a la lista y ordenarla por nombre de canción
def add_song_and_sort(songs, new_song):
    songs.append(new_song)
    return sort_songs(songs, "cancion")

# Función para determinar cuántas canciones de una banda específica hay en la lista
def count_songs_by_artist(songs, artist):
    return sum(1 for song in songs if song["banda_artista"] == artist)

# Función para mostrar toda la información de una canción específica
def find_song_info(songs, song_name):
    for song in songs:
        if song["nombre"] == song_name:
            return song
    return None

# Ejecutar las funciones y mostrar los resultados
print("Listado ordenado por canción:")
for song in sort_songs(songs, "cancion"):
    print(song)

print("\nListado ordenado por banda o artista:")
for song in sort_songs(songs, "banda_artista"):
    print(song)

print("\nListado ordenado por año de lanzamiento:")
for song in sort_songs(songs, "año_lanzamiento"):
    print(song)

print("\n¿Hay alguna canción de Audioslave en la lista?:", find_songs_by_artist(songs, "Audioslave"))
print("¿Hay alguna canción de The Rolling Stones en la lista?:", find_songs_by_artist(songs, "The Rolling Stones"))

print("\nTodas las canciones de Nirvana:")
for song in songs_by_artist(songs, "Nirvana"):
    print(song)

new_song = {"nombre": "Highway to Hell", "banda_artista": "AC/DC", "año_lanzamiento": 1979}
print("\nAgregando la canción 'Highway to Hell' y volviendo a ordenar por nombre de canción:")
for song in add_song_and_sort(songs, new_song):
    print(song)

print("\nCantidad de canciones de Red Hot Chili Peppers en la lista:", count_songs_by_artist(songs, "Red Hot Chili Peppers"))

print("\nInformación de la canción 'Fake tales of San Francisco':")
print(find_song_info(songs, "Fake tales of San Francisco"))
print("\nInformación de la canción 'Black hole sun':")
print(find_song_info(songs, "Black hole sun"))
