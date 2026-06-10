class Song:
    count = 0
    genres = []
    artists = []
    genre_count = 0
    artists_count = 0
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
