class Song:
    # Class attributes shared by every Song object
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes unique to each song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the shared class attributes
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs."""
        cls.count += 1

    def add_to_genres(self):
        """Add a genre only if it is not already recorded."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Add an artist only if they are not already recorded."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Count the number of songs belonging to each genre."""
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1

    def add_to_artists_count(self):
        """Count the number of songs belonging to each artist."""
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1
