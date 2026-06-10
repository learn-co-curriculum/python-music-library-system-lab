class Song:
    """Represent a song and maintain shared library analytics."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update library-wide state whenever a new Song instance is created
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of Song instances."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the shared genre list if it is not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the shared artist list if it is not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the song count for a genre, adding the genre if needed."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the song count for an artist, adding the artist if needed."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
