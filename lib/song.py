class Song:
    song_count = 0
    genre_count = {}
    artists_count = {}
    genres = []
    artists =[]

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.song_count += 1

        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        Song.artists_count[artist] = Song.artists_count.get(artist, 0) + 1

    @classmethod
    def count(cls):
        return cls.song_count

    @classmethod
    def genres(cls):
        return list(cls.genre_count.keys())

    @classmethod
    def artists(cls):
        return list(cls.artists_count.keys())
    
    @classmethod
    def add_song_to_count(cls, song):
        cls.song_count += 1
    
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
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1

s1 = Song("Halo", "Beyonce", "Pop")
s2 = Song("Crazy in Love", "Beyonce", "R&B")

print(Song.count())  # Output: 2
print(Song.genres())  # Output: ['Pop', 'R&B']
print(Song.artists())  # Output: ['Beyonce']
print(Song.genre_count)  # Output: {'Pop': 1, 'R&B': 1}
