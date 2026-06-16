class Song:
    """Song class to track song instances and aggregate data.

    Instance attributes
    - name: title of the song
    - artist: artist name
    - genre: genre name

    Class attributes (shared across all Song instances)
    - count: total number of Song instances created
    - genres: list of unique genres seen
    - artists: list of unique artists seen
    - genre_count: mapping of genre -> number of songs for that genre
    - artist_count: mapping of artist -> number of songs for that artist
    - songs: list of Song instances created
    """

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    songs = []

    def __init__(self, name, artist, genre):
        # Save instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level trackers
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artists_count(self.artist)

        # Keep a registry of created Song objects
        Song.songs.append(self)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the unique genres list if not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the unique artists list if not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count for a genre; initialize to 1 if missing."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the count for an artist; initialize to 1 if missing."""
        # Note: tests expect the class attribute to be named `artist_count`.
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    def __repr__(self):
        return f"<Song name={self.name!r} artist={self.artist!r} genre={self.genre!r}>"
