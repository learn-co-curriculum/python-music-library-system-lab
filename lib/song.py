name = input("Enter the song title: ")
genre = input("Enter the song genre: ")
artist = input("Enter the artist: ")

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

    @classmethod
    def add_song_to_count(cls, count):
        count += 1
        return count

    @classmethod
    def add_to_genres(cls, genre_count):
        for genre in cls.genres:
            if len(cls.genres) != len(cls.genres):
                return genre_count
