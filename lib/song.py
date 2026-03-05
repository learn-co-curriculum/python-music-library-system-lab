class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        Song.genres.append(genre)

        Song.artists.append(artist)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

# TEST
s1 = Song("Halo", "Beyonce", "Pop")
s2 = Song("Imagine", "John Lennon", "Rock")
s3 = Song("Single Ladies", "Beyonce", "Pop")

print("Song count:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)