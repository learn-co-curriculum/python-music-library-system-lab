class Song:
    """
    Represents a song in the music library system.
    Tracks global statistics across all Song objects.
    """

    # -------------------------
    # CLASS ATTRIBUTES
    # -------------------------
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    # -------------------------
    # INITIALIZER
    # -------------------------
    def __init__(self, name, artist, genre):
        """
        Creates a new Song instance and updates
        all class-level tracking attributes.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger tracking updates automatically
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # -------------------------
    # CLASS METHODS
    # -------------------------
    @classmethod
    def add_song_to_count(cls):
        """Increment total song count."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre if it doesn't already exist."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist if it doesn't already exist."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Increment genre count.
        If genre doesn't exist yet, initialize it to 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Increment artist count.
        If artist doesn't exist yet, initialize it to 1.
        """
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    
