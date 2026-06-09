class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        #initializing new song object 
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(cls):
        #incrementing total by 1
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, genre):
        #adding genre to the set of genres
        cls.genres.add(genre)
        
    @classmethod
    def add_to_artists(cls, artist):
        #adding artist to the set of artists
        cls.artists.add(artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
        #update the genre_count dictionary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1 #if genre exists it increments by 1
        else:
            cls.genre_count[genre] = 1 #if not it initializes with 1
            
    @classmethod
    def add_to_artist_count(cls, artist):
        #update artists_count dictionary
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1 #if artist exists it increments by 1
        else:
            cls.artist_count[artist] = 1 #if not it initializes with 1
            
    @classmethod
    def show_library_info(cls):
        # display insights about the song library
        print(f"Total songs: {cls.count}")
        print(f"Artists: {cls.artists}")
        print(f"Genre: {cls.genres}")
        print(f"Genre counts: {cls.genre_count}")
        print(f"Artist counts: {cls.artist_count}")                                