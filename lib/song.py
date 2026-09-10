class Song:
    # Class attributes shared by every Song object.
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        # Store the information for this individual song.
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-wide song information.
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increase the total number of songs by one.
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add the genre only if it is not already in the list.
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add the artist only if they are not already in the list.
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add a new genre with a count of 1,
        # or increment the existing genre count.
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Add a new artist with a count of 1,
        # or increment the existing artist count.
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

        # Keep both attribute names synchronized.
        cls.artists_count = cls.artist_count
