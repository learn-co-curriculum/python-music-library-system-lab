class Song:
    pass
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods on every new song creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # ── Class Methods ──────────────────────────────────────────────────────────

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a genre to the genres list if it isn't already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds an artist to the artists list if they aren't already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments the count for a genre; adds it with value 1 if new."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increments the count for an artist; adds them with value 1 if new."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    # ── String Representation ──────────────────────────────────────────────────

    def __repr__(self):
        return f"Song(name='{self.name}', artist='{self.artist}', genre='{self.genre}')"


# ── Demo ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Create some songs
    s1 = Song("Halo",          "Beyonce",   "Pop")
    s2 = Song("Crazy in Love", "Beyonce",   "Pop")
    s3 = Song("99 Problems",   "Jay-Z",     "Rap")
    s4 = Song("Empire State",  "Jay-Z",     "Rap")
    s5 = Song("Old Town Road", "Lil Nas X", "Country")
    s6 = Song("Rockstar",      "Post Malone","Rap")

    print("=== Song Class Attributes ===")
    print(f"Total songs    : {Song.count}")
    print(f"Unique genres  : {Song.genres}")
    print(f"Unique artists : {Song.artists}")
    print(f"Songs per genre: {Song.genre_count}")
    print(f"Songs per artist:{Song.artists_count}")
    print()
    print("=== Individual Song Objects ===")
    for song in [s1, s2, s3, s4, s5, s6]:
        print(song)