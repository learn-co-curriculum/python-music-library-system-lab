class Song:
    # pass

    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods whenever a new song is created
        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increase the total number of songs by 1.
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add a genre if it doesn't already exist.
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add an artist if they don't already exist.
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Track how many songs belong to each genre.
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Track how many songs each artist has.
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1