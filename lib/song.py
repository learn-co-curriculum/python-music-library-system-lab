class Song:
    """A class to represent a Song and collect global song statistics.

    Each instance stores `name`, `artist`, and `genre` for a single song.
    The class also maintains aggregate data across all Song instances:
      - `count`: total number of Song instances created
      - `genres`: list of unique genres seen
      - `artists`: list of unique artists seen
      - `genre_count`: mapping genre -> number of songs in that genre
      - `artist_count`: mapping artist -> number of songs by that artist
    """

    # Class attributes for global tracking
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Instantiate a Song and update class-level statistics.

        All class-updating helper methods are called so creating a Song
        automatically updates global counters and collections.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level trackers
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total Song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add `genre` to the list of known genres if it's new."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add `artist` to the list of known artists if it's new."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the count for `genre`, creating the key if needed."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment the count for `artist`, creating the key if needed."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
