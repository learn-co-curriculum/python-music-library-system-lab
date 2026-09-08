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
 
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
 
    def __repr__(self):
        return f"<Song name={self.name!r} artist={self.artist!r} genre={self.genre!r}>"
 
    
    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1
 
    @classmethod
    def add_to_genres(cls, genre):
        """Adds a new genre to the genres list. Ensures uniqueness."""
        if genre not in cls.genres:
            cls.genres.append(genre)
 
    @classmethod
    def add_to_artists(cls, artist):
        """Adds a new artist to the artists list. Ensures uniqueness."""
        if artist not in cls.artists:
            cls.artists.append(artist)
 
    @classmethod
    def add_to_genre_count(cls, genre):
        """Increments genre_count for the given genre, creating the key if needed."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
 
    @classmethod
    def add_to_artist_count(cls, artist):
        """Increments artist_count for the given artist, creating the key if needed."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
