class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Helicopter", "ASAP Rocky", "Rap")
song3 = Song("Crazy in Love", "Beyonce", "Pop")
song4 = Song("Ran to Atlanta", "Drake", "Rap")
song5 = Song("Niggas in Paris", "Jay Z", "Rap")
song2 = Song("Empire State of Mind", "Jay Z", "Rap")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)