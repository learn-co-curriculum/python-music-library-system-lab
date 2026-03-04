class Song:
    count = 0
    genres = []
    artists = []
    genre_count = []
    artists_count = []
    
def __init__(self, name, artist, genre):
    self.name = name
    self.artist = artist
    self.genre = genre
    
    Song.add_song_to_count()
    Song.add_to_genre(genre)
    Song.add_to_artist(artist)
    Song.add_to_genre_count(genre)
    Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)