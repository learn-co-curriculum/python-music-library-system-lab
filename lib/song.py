# song.py
# Music Library System - Song Class
# Manages individual song data and tracks global library statistics.

class Song:
    # --- Class Attributes ---
    count = 0           # Total number of songs created
    genres = []         # List of unique genres
    artists = []        # List of unique artists
    genre_count = {}    # Number of songs per genre e.g. {"Pop": 3, "Rap": 2}
    artists_count = {}  # Number of songs per artist e.g. {"Beyonce": 17}

    def __init__(self, name, artist, genre):
        # Instance attributes for each song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Automatically update class-level stats when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments total song count by 1 each time a song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds genre to genres list only if it doesn't already exist (no duplicates)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds artist to artists list only if it doesn't already exist (no duplicates)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments genre count by 1, or initializes it to 1 if not yet tracked."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increments artist count by 1, or initializes it to 1 if not yet tracked."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1