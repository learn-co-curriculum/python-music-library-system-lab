# Song class - Represents a song in the music library

class Song:
    # Class attributes (shared across all instances)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes (unique to each song)
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call class methods when new song is created
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        # Increment total song count by 1
        cls.count += 1
    
    def add_to_genres(self):
        # Add genre to list if not already there
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
    
    def add_to_artists(self):
        # Add artist to list if not already there
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
    
    def add_to_genre_count(self):
        # Increment genre count or add new genre with count 1
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
    
    def add_to_artist_count(self):
        # Increment artist count or add new artist with count 1
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1