#!/usr/bin/env python3

import unittest
from lib.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        Song.count = 0
        Song.genres = []
        Song.artists = []
        Song.genre_count = {}
        Song.artists_count = {}

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Out of Touch", "Hall and Oates", "Pop")
        Song("Sara Smile", "Hall and Oates", "Pop")

    def test_saves_name_artist_genre(self):
        song = Song("Test Track", "Test Artist", "Test Genre")
        self.assertEqual(song.name, "Test Track")
        self.assertEqual(song.artist, "Test Artist")
        self.assertEqual(song.genre, "Test Genre")

    def test_has_song_count(self):
        self.assertEqual(Song.count, 5)

    def test_has_genres(self):
        self.assertIn("Rap", Song.genres)
        self.assertIn("Pop", Song.genres)
        self.assertIn("Rock", Song.genres)

    def test_has_artists(self):
        self.assertIn("Jay Z", Song.artists)
        self.assertIn("Beyonce", Song.artists)
        self.assertIn("Hall and Oates", Song.artists)

    def test_has_genre_count(self):
        self.assertEqual(Song.genre_count["Rap"], 1)
        self.assertEqual(Song.genre_count["Pop"], 3)
        self.assertEqual(Song.genre_count["Rock"], 1)

    def test_has_artist_count(self):
        self.assertEqual(Song.artists_count["Jay Z"], 1)
        self.assertEqual(Song.artists_count["Beyonce"], 1)
        self.assertEqual(Song.artists_count["Nirvana"], 1)
        self.assertEqual(Song.artists_count["Hall and Oates"], 2)

if __name__ == "__main__":
    unittest.main()
