class Song:
    count =0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    
    def __init__(self,name,artist,genre):
         if genre not in Song.genres:
             Song.genres.append(genre)
         if artist not in Song.artists:
             Song.artists.append(artist)
         if genre not in Song.genre_count:
             Song.genre_count[genre] =1
         else:
             Song.genre_count[genre] +=1

         if artist not in Song.artist_count:
             Song.artist_count[artist] =1
         else:
             Song.artist_count[artist] +=1


         
         self.name = name
         self.artist = artist
         self.genre = genre
         Song.count += 1

    def add_song_to_count(self,count):
        pass
       


    def add_to_genres(self,genres):
        pass
    
    
    def add_to_artists(self,artists):
        if artists not in self.artist:
            self.artist.append(artists)


    def add_to_genre_count(self,genre_count):
        pass


    def add_to_artists_count(self,artists_count):
        pass
