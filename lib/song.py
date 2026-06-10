name = input("Enter the song title: ")
genre = input("Enter the song genre: ")
artist = input("Enter the artist: ")

class Song:
    count = 0
    all_songs = {}
    genres = []
    artists = []
    genre_count = 0
    artists_count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all_songs.append(self)

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1
        return Song.count

    @classmethod
    def add_to_genres(cls, genres):
        for genre in cls.genres:
            if len(cls.genres) != len(cls.genres):
                return genres
        
        genres += 1
            
    @classmethod
    def add_to_artists(cls, artists):
        for genre in cls.artists:
            if len(cls.artists) != len(cls.artists):
                return artists
            
        artists += 1

    @classmethod
    def add_to_genre_count(cls, genre, genre_count):
        genre_count += 1
        return [f"{genre}: {genre_count}"]