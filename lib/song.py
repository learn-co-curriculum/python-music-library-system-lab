class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name: str, artist: str, genre: str):
        """
        Initializes a new Song instance and automatically updates global class tracking.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total value of created songs by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        """Adds new genres to the genres list, ensuring no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        """Adds new artists to the artists list, ensuring no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        """Increments genre key by 1, or initializes it to 1 if it doesn't exist."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist: str):
        """Increments artist key by 1, or initializes it to 1 if it doesn't exist."""
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1


if __name__ == "__main__":

    song1 = Song("Halo", "Beyonce", "Pop")
    song2 = Song("Single Ladies", "Beyonce", "Pop")
    song3 = Song("Empire State of Mind", "Jay-Z", "Rap")
    song4 = Song("Texas Hold 'Em", "Beyonce", "Country")

    print(f"Total Songs Created: {Song.count}")
    print(f"Unique Artists: {Song.artists}")
    print(f"Unique Genres: {Song.genres}")
    print(f"Genre Distribution: {Song.genre_count}")
    print(f"Artist Song Counts: {Song.artists_count}")
