class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    # Constructor
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Use class methods (important requirement)
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # Class methods
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
            