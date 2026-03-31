# Python Music Library System Lab

## Overview

This project implements a **`Song` class** in Python that represents individual songs and tracks global statistics about the music library. It is designed to make it easy to manage and analyze a collection of songs for a music streaming service.

---

## Song Class

The `Song` class allows users to:

- Create a song object with a `name`, `artist`, and `genre`.
- Automatically update **global statistics** about all songs.
- Retrieve a summary of all songs, artists, genres, and counts.

### Class Attributes

The `Song` class keeps track of:

| Attribute       | Description                                           |
|-----------------|-------------------------------------------------------|
| `count`         | Total number of `Song` instances created             |
| `artists`       | Set of all unique artists                             |
| `genres`        | Set of all unique genres                              |
| `artist_count`  | Dictionary counting number of songs per artist       |
| `genre_count`   | Dictionary counting number of songs per genre        |

---

### Usage Example

```python
from lib.song import Song


s1 = Song("Shape of You", "Ed Sheeran", "Pop")
s2 = Song("Blinding Lights", "The Weeknd", "R&B")
s3 = Song("Perfect", "Ed Sheeran", "Pop")
s4 = Song("Rockstar", "Post Malone", "Rap")


print(Song.all_songs_info())

# Setup
follow this steps to access this application

clone the repository on your terminal
git clone 

navigate into the directory
cd python-music-libray-system

install all dependancies
npm install

run  pytest to see all test that have passed

# ScreenShot
![alt text](<Screenshot from 2026-03-31 22-32-20.png>)


# Author 
Fatuma Asman 