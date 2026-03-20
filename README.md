# 🎵 Song Class – Music Library System

## Overview

This project implements a `Song` class that models a simple music library system. It tracks individual songs and maintains aggregated data such as total songs, genres, and artists.done

## Attributes

### Instance Attributes

* `name` – Name of the song
* `artist` – Artist of the song
* `genre` – Genre of the song

### Class Attributes

* `count` – Total number of songs created
* `genres` – List of all song genres
* `artists` – List of all song artists
* `genre_count` – Dictionary tracking number of songs per genre
* `artists_count` – Dictionary tracking number of songs per artist

---

## Class Methods

* `add_song_to_count()` – Increments total song count
* `add_to_genres(genre)` – Adds a genre to the list
* `add_to_artists(artist)` – Adds an artist to the list
* `add_to_genre_count(genre)` – Tracks number of songs per genre
* `add_to_artists_count(artist)` – Tracks number of songs per artist

---

## Behavior

When a new `Song` object is created:

* The total song count is updated
* The genre and artist are recorded
* The counts for that genre and artist are updated

All updates are handled automatically through class methods.

---

## Example Usage

```python
song1 = Song("Empire State of Mind", "Jay Z", "Rap")

print(Song.count)           # 1
print(Song.genres)          # ['Rap']
print(Song.artists)         # ['Jay Z']
print(Song.genre_count)     # {'Rap': 1}
print(Song.artists_count)   # {'Jay Z': 1}
```

---

## Testing

This project uses `pytest` to verify functionality.
Run tests with:

```bash
pytest song_test.py
```

---
