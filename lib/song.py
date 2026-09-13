class Song:
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
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 0
        Song.genre_count[self.genre] += 1

    def add_to_artists_count(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 0
        Song.artist_count[self.artist] += 1
        Song.artists_count = Song.artist_count
