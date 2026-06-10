name = input("Enter the song title: ")
genre = input("Enter the song genre: ")
artist = input("Enter the artist: ")

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.all_songs.append(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre, genre_count):
        genre_count += 1
        return [f"{genre}: {genre_count}"]
    
    @classmethod
    def add_to_artists_count(cls, artist, artists_count):
        artists_count += 1
        return [f"{artist}: {artists_count}"]