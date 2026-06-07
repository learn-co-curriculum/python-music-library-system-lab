class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    
    artist_count = {} 

    def __init__(self, name, artist, genre):
        """
        Initialize a new Song instance.
        Sets the instance attributes and triggers class methods to update class-level data.
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        
        
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds any new genres to the class attribute genres.
        Ensures there are only unique genres (no duplicates).
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds any new artists to the class attribute artists.
        Ensures there are only unique artists (no duplicates).
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates class attribute genre_count.
        Increments genre key by 1; if genre doesn't exist, adds the key and sets it to 1.
        """
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Updates class attribute artist_count.
        Increments artist key by 1; if artist doesn't exist, adds the key and sets it to 1.
        """
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1