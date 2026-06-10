class Song:
    # --- Class Attributes ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods automatically upon instantiation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        """Increments the global song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a new genre to the unique genres list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds a new artist to the unique artists list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments the genre tally, initializing it to 1 if new."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increments the artist tally, initializing it to 1 if new."""
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1