#!/usr/bin/env python3
from lib.song import Song
import sys

# Reset class state to known values
Song.count = 0
Song.genre_count = {}
Song.artist_count = {}
Song.genres = []
Song.artists = []
Song.songs = []

# Create initial songs (mirrors lib/testing/song_test.py)
Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")

try:
    # test_saves_name_artist_genre
    out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
    assert(out_of_touch.name == "Out of Touch")
    assert(out_of_touch.artist == "Hall and Oates")
    assert(out_of_touch.genre == "Pop")

    # test_has_song_count
    assert(Song.count == 4)
    Song("Sara Smile", "Hall and Oates", "Pop")
    assert(Song.count == 5)

    # test_has_genres
    assert("Rap" in Song.genres)
    assert("Pop" in Song.genres)
    assert("Rock" in Song.genres)

    # test_has_artists
    assert("Jay Z" in Song.artists)
    assert("Beyonce" in Song.artists)
    assert("Hall and Oates" in Song.artists)

    # test_has_genre_count
    assert(Song.genre_count["Rap"] == 1)
    assert(Song.genre_count["Pop"] == 3)
    assert(Song.genre_count["Rock"] == 1)

    # test_has_artist_count
    assert(Song.artist_count["Jay Z"] == 1)
    assert(Song.artist_count["Beyonce"] == 1)
    assert(Song.artist_count["Nirvana"] == 1)
    assert(Song.artist_count["Hall and Oates"] == 2)

except AssertionError as e:
    print("One or more assertions failed")
    raise

print("All tests passed")
