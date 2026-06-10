# Song Analytics Application

## Overview

The Song Analytics Application is a Python-based project that models songs and provides insights about a music collection. It allows users to create song objects while automatically tracking important statistics such as the total number of songs, unique artists, unique genres, and song counts by artist and genre.

This functionality can be useful for music libraries, recommendation systems, streaming platforms, and data analytics applications.

## Features

* Create and manage song objects.
* Store song information including:

  * Name
  * Artist
  * Genre
* Automatically track:

  * Total number of songs created
  * Unique artists
  * Unique genres
  * Number of songs per artist
  * Number of songs per genre

## Class Structure

### Song

#### Instance Attributes

| Attribute | Description                   |
| --------- | ----------------------------- |
| `name`    | Name of the song              |
| `artist`  | Artist who performed the song |
| `genre`   | Genre of the song             |

#### Class Attributes

| Attribute       | Description                          |
| --------------- | ------------------------------------ |
| `count`         | Total number of songs created        |
| `genres`        | List of unique genres                |
| `artists`       | List of unique artists               |
| `genre_count`   | Dictionary tracking songs per genre  |
| `artists_count` | Dictionary tracking songs per artist |

## Class Methods

### `add_song_to_count()`

Increments the total song count by one.

### `add_to_genres(genre)`

Adds a genre to the list of genres if it does not already exist.

### `add_to_artists(artist)`

Adds an artist to the list of artists if they do not already exist.

### `add_to_genre_count(genre)`

Updates the count of songs for a specific genre.

### `add_to_artists_count(artist)`

Updates the count of songs for a specific artist.

## Example Usage

```python
song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Empire State of Mind", "Jay-Z", "Rap")
song3 = Song("Single Ladies", "Beyonce", "Pop")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artists_count)
```

### Output

```python
3
['Pop', 'Rap']
['Beyonce', 'Jay-Z']
{'Pop': 2, 'Rap': 1}
{'Beyonce': 2, 'Jay-Z': 1}
```

## Learning Objectives

* Understand Python classes and objects.
* Work with instance and class attributes.
* Implement class methods using the `@classmethod` decorator.
* Track and aggregate data across multiple object instances.
* Use dictionaries and lists to store analytical information.

### Image Display

Screenshot 2026-06-10 232508.png

## Technologies Used

* Python 3

## Author

Developed as an object-oriented programming exercise focused on class design and data tracking.



