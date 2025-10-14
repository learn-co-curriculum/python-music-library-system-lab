class Song:
    count = 0                   # total number of Song objects created
    genres = []                 # unique list of all genres seen
    artists = []                # unique list of all artists seen
    genre_count = {}            # {"Pop": 3, "Rap": 1, ...}
    artist_count = {}           # {"Beyonce": 2, "Jay Z": 1, ...}

    def __init__(self, name, artist, genre):
        """
        Create a new Song.
        name   -> song title (str)
        artist -> artist/band name (str)
        genre  -> genre name (str)
        """
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update global (class-level) analytics every time a Song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increase the total number of Song objects by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a new genre to the class list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add a new artist to the class list if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the counter for the given genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the counter for the given artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1