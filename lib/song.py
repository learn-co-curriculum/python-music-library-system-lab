class Song:

    # class attributes shared by every Song instance
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # every time a new song is made, update all the tracking info
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        # bump the total song counter
        Song.count += 1

    def add_to_genres(self):
        # only add the genre if we haven't seen it before
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        # only add the artist if we haven't seen them before
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # if the genre is new, start it at 1, otherwise add 1
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        # if the artist is new, start them at 1, otherwise add 1
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1