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