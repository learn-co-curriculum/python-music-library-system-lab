class Song:
    # keeps track of all songs and their details
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    artist_count = artists_count  # test uses this name

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # update all trackers when a new song is made
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        # increase total song count
        Song.count += 1

    def add_to_genres(self):
        # add genre if it's not already in the list
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        # add artist if not already there
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # count how many songs per genre
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists_count(self):
        # count how many songs per artist
        if self.artist in Song.artists_count:
            Song.artists_count[self.artist] += 1
        else:
            Song.artists_count[self.artist] = 1
        Song.artist_count = Song.artists_count

    # some tests call this name instead
    def add_to_artist_count(self):
        self.add_to_artists_count()
