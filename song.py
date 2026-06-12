class Song:
    # --- Class Attributes ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # --- Instance Attributes ---
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Automatically trigger class tracking updates on creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds new unique genres to the genres list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds new unique artists to the artists list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments genre key by 1. If it doesn't exist, initializes it to 1."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increments artists key by 1. If it doesn't exist, initializes it to 1."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1