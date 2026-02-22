# song.py

class Song:
    # Class attributes (the tests expect these exact names)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level tracking
        Song.count += 1

        #Track unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        #Track unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        #Count songs per genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        #Count songs per artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1