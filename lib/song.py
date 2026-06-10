class Song:
    # --- Class Attributes ---
    count = 0
    genres = []          # Keeps track of unique genres
    artists = []         # Keeps track of unique artists
    genre_count = {}     # Format: {"Rap": 5, "Rock": 1}
    artists_count = {}   # Format: {"Beyonce": 17, "Jay-Z": 40}

    def __init__(self, name: str, artist: str, genre: str):
        # --- Instance Attributes ---
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # --- Automated Method Triggers ---
        # Automatically run class methods upon instantiation
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        """Increments the total value of song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        """Adds new genres to the unique genres list without duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        """Adds new artists to the unique artists list without duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        """Increments genre key by 1. Adds it if it doesn't exist."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist: str):
        """Increments artist key by 1. Adds it if it doesn't exist."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1