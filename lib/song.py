class Song:
    pass
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
        
        cls = self.__class__
        cls.count += 1
        
        if genre not in cls.genres:
            cls.genres.append(genre)
            
        if artist not in cls.artists:
            cls.artists.append(artist)
            
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1

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
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1