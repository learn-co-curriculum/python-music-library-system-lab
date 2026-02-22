# Music Library System Lab  
## Inheritance, Class Attributes, and Class Methods 

---

## Overview

This lab implements a `Song` class in Python that models individual songs while maintaining global statistics across all song instances.

The objective of this lab was to practice:

- Object-Oriented Programming (OOP)
- Class attributes
- Class methods
- Instance attributes
- Shared state management
- Automated testing with Pytest

---

## Project Description

The `Song` class represents individual songs with the following attributes:

- `name`
- `artist`
- `genre`

In addition to representing individual songs, the class maintains global insights about all songs created during runtime.

The system automatically tracks:

- Total number of songs created
- All unique genres
- All unique artists
- Number of songs per genre
- Number of songs per artist

This demonstrates how class-level attributes can maintain shared state across multiple instances.

---

## Features Implemented

### Instance Attributes

Each `Song` object stores:

- `name`
- `artist`
- `genre`

### Class Attributes

The class maintains:

- `count` → Total number of songs created  
- `genres` → List of unique genres  
- `artists` → List of unique artists  
- `genre_count` → Dictionary tracking songs per genre  
- `artist_count` → Dictionary tracking songs per artist  

### Automatic Updates

Whenever a new `Song` is instantiated:

- Total count increases
- Genre is added (if unique)
- Artist is added (if unique)
- Genre count updates
- Artist count updates

All tracking happens automatically during object creation.

---

## Example Usage

```python
from song import Song

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

print(Song.count)
print(Song.genres)
print(Song.genre_count)
print(Song.artist_count)
```

---

## How to Run the Project

### 1. Install dependencies

```bash
pipenv --python 3.12
pipenv install --dev
```

### 2. Run the tests

```bash
pipenv run pytest -x
```

Expected output:

```
6 passed
```

---

## Testing

All functionality was verified using Pytest.

The tests confirm:

- Songs instantiate correctly
- Song count increments properly
- Unique genres are tracked
- Unique artists are tracked
- Genre counts are accurate
- Artist counts are accurate

All test cases pass successfully.

---

## Screenshot of Completed Work

Below is the test result showing all tests passing:

![Test Results](test-results.png)

*(Ensure `test-results.png` is located in the root directory of the project before pushing to GitHub.)*

---

## Key Concepts Demonstrated

- Difference between instance attributes and class attributes
- Use of `@classmethod`
- Shared state across objects
- Dictionary-based counting logic
- Clean OOP design
- Automated testing

---

## Conclusion

This lab successfully demonstrates how class attributes and class methods can be used to maintain shared data across multiple object instances in Python.

The `Song` class now:

- Tracks total songs
- Stores unique artists and genres
- Maintains accurate count mappings
- Passes all provided tests

This reinforces foundational Object-Oriented Programming principles in Python.