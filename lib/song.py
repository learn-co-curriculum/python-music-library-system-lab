# lib/song.py

class Song:
    # -----------------------------
    # Class attributes (global stats)
    # -----------------------------
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    # -----------------------------
    # Instance initialization
    # -----------------------------
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level statistics
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    # -----------------------------
    # Methods to update global stats
    # -----------------------------
    def add_song_to_count(self):
        Song.count += 1

    def add_to_genres(self):
        Song.genres.add(self.genre)

    def add_to_artists(self):
        Song.artists.add(self.artist)

    def add_to_genre_count(self):
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1

    def add_to_artist_count(self):
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1

    # -----------------------------
    # Class method to show all songs info
    # -----------------------------
    @classmethod
    def all_songs_info(cls):
        return {
            "Total Songs": cls.count,
            "Artists": list(cls.artists),
            "Genres": list(cls.genres),
            "Songs by Genre": cls.genre_count,
            "Songs by Artist": cls.artist_count,
        }

    # -----------------------------
    # String representation for printing
    # -----------------------------
    def __str__(self):
        return f"'{self.name}' by {self.artist} [{self.genre}]"