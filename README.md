# Music Library System

A Python class-based music library that tracks songs and provides global insights across the entire collection.

## Features

- Create song objects with a name, artist, and genre
- Automatically tracks:
  - Total number of songs
  - All unique artists
  - All unique genres
  - Song count per genre
  - Song count per artist

## Usage

```python
from song import Song

s1 = Song("Blinding Lights", "The Weeknd", "Pop")
s2 = Song("Starboy", "The Weeknd", "Pop")
s3 = Song("HUMBLE.", "Kendrick Lamar", "Hip-Hop")

print(Song.count)          # 3
print(Song.artists)        # ['The Weeknd', 'Kendrick Lamar']
print(Song.genres)         # ['Pop', 'Hip-Hop']
print(Song.genre_count)    # {'Pop': 2, 'Hip-Hop': 1}
print(Song.artists_count)  # {'The Weeknd': 2, 'Kendrick Lamar': 1}
```

## Class Structure

| Type | Name | Description |
|------|------|-------------|
| Instance Attribute | `name` | Song title |
| Instance Attribute | `artist` | Artist name |
| Instance Attribute | `genre` | Song genre |
| Class Attribute | `count` | Total songs created |
| Class Attribute | `genres` | Unique genres list |
| Class Attribute | `artists` | Unique artists list |
| Class Attribute | `genre_count` | Songs per genre |
| Class Attribute | `artists_count` | Songs per artist |
| Class Method | `add_song_to_count()` | Increments count |
| Class Method | `add_to_genres()` | Updates genres list |
| Class Method | `add_to_artists()` | Updates artists list |
| Class Method | `add_to_genre_count()` | Updates genre_count |
| Class Method | `add_to_artists_count()` | Updates artists_count |

## Screenshot

![Music Library System](screenshot.png)