class Song:
    song_count = 0
    song_genre = []
    song_artist = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    def get_details(self):
        return f'Name : {self.name} , Artist : {self.artist}, Genre : {self.genre}'
    
    @classmethod
    def add_song_to_count(cls):
        cls.song_count +=1
    
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.song_genre:
            cls.song_genre.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.song_artist:
            cls.song_artist.append(artist)
        
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] +=1
        else:
            cls.genre_count[genre] =1 
    @classmethod
    def add_to_artists_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else:
            cls.artist_count[artist] =1


song1 = Song('Nairobi', 'Buruklyn Boyz', 'Hiphop')
song2 = Song('Chinje', 'Toxic Lyrikali', 'Hiphop')
song3 = Song('Solo', 'Future', 'Bongo')
song4 = Song('58', 'Buruklyn Boyz', 'Hiphop')


print(Song.genre_count)
print(Song.artist_count)

