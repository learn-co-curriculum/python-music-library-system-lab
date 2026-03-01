class Song:
    # Class Attributes (Global State)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger class methods upon creation
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total count of songs."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a unique genre to the global list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds a unique artist to the global list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Tracks how many songs belong to each genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Tracks how many songs each artist is responsible for."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

# --- Testing the Implementation ---
if __name__ == "__main__":
    s1 = Song("Single Ladies", "Beyonce", "Pop")
    s2 = Song("Halo", "Beyonce", "Pop")
    s3 = Song("Empire State of Mind", "Jay-Z", "Hip Hop")

    print(f"Total Songs: {Song.count}")
    print(f"Unique Genres: {Song.genres}")
    print(f"Genre Breakdown: {Song.genre_count}")
    print(f"Artist Breakdown: {Song.artists_count}")