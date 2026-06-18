class Song:
    # Class attributes shared across every Song instance.
    # These give us global insights into the whole music library.
    count = 0            # total number of Song objects created
    genres = []          # list of all unique genres
    artists = []         # list of all unique artists
    genre_count = {}     # number of songs per genre  -> {"Rap": 5, "Rock": 1}
    artist_count = {}    # number of songs per artist  -> {"Beyonce": 17}

    def __init__(self, name, artist, genre):
        # Instance attributes describing this particular song.
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every time a song is created, update the global library data.
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        '''Increment the total number of songs by one.'''
        Song.count += 1

    def add_to_genres(self):
        '''Add this song's genre to the list of unique genres.'''
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        '''Add this song's artist to the list of unique artists.'''
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        '''Track how many songs belong to each genre.'''
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        '''Track how many songs each artist is responsible for.'''
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1