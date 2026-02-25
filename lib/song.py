class Song:
    
    # -----------------------------
    # Class Attributes
    # -----------------------------
    
    # Total number of songs created
    count = 0
    
    # Unique list of genres
    genres = []
    
    # Unique list of artists
    artists = []
    
    # Dictionary to track number of songs per genre
    genre_count = {}
    
    # Dictionary to track number of songs per artist
    artists_count = {}

    # -----------------------------
    # Constructor
    # -----------------------------
    def __init__(self, name, artist, genre):
        """
        Initializes a new Song object.
        Automatically updates all tracking class attributes.
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger class methods upon song creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # -----------------------------
    # Class Methods
    # -----------------------------
    
    @classmethod
    def add_song_to_count(cls):
        """Increment total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add genre to genres list if it does not already exist."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add artist to artists list if it does not already exist."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Increment genre count.
        If genre does not exist, initialize it with 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Increment artist count.
        If artist does not exist, initialize it with 1.
        """
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    # -----------------------------
    # Utility Method
    # -----------------------------
    
    @classmethod
    def display_summary(cls):
        """Display summary information about all songs."""
        print("Total Songs:", cls.count)
        print("Artists:", cls.artists)
        print("Genres:", cls.genres)
        print("Songs per Genre:", cls.genre_count)
        print("Songs per Artist:", cls.artists_count)
   # pass
