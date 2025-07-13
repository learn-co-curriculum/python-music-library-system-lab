class Song:
    #class attributes to track global song info
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__ (self, name, artist, genre):
        #instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        #updates class lvl tracking the moment an instance is created
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    #keeping track of total nr of songs created
    @classmethod
    def add_song_to_count(cls):
        cls.count+=1

   #adding every new genre to the list of genres
    @classmethod
    def add_to_genres(cls, unique_genre):
        if unique_genre not in cls.genres:
                cls.genres.append(unique_genre)

    #adding every new artist to list of artists
    @classmethod
    def add_to_artists(cls, unique_artist):
        if unique_artist not in cls.artists:
            cls.artists.append(unique_artist)

    #incrementing the song count for a genre
    @classmethod
    def add_to_genre_count(cls, unique_genre):
        if unique_genre not in cls.genre_count:
            cls.genre_count[unique_genre] = 0
        cls.genre_count[unique_genre] += 1

    #incrementing the song count for an artist
    @classmethod
    def add_to_artists_count(cls, unique_artist):
        if unique_artist not in cls.artist_count:
            cls.artist_count[unique_artist] = 0
        cls.artist_count[unique_artist] += 1