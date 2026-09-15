class Song:
    # Class Attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    artist_count = {}  # Added to match test suite expectations

    def __init__(self, name, artist, genre):
        """Initialize instance attributes and trigger class methods."""
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods upon initialization
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds unique genres to the genres list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds unique artists to the artists list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates frequency of songs per genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Updates frequency of songs per artist."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
            
        # Update singular attribute to satisfy test suite
        cls.artist_count[artist] = cls.artists_count[artist]

