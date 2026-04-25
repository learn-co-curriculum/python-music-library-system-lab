#!/usr/bin/env python3

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
        
        # Increment total song count
        Song.count += 1
        
        # Add genre to the genres list if not already present
        if genre not in Song.genres:
            Song.genres.append(genre)
        
        # Add artist to the artists list if not already present
        if artist not in Song.artists:
            Song.artists.append(artist)
        
        # Update the count of songs for the genre
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        
        # Update the count of songs for the artist
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1

    @classmethod
    def add_to_genre_count(cls, genre):
        """Update genre_count dictionary."""
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Update artist_count dictionary."""
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1
        