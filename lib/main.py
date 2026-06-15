from song import Song

def main():
    song1 = Song("Incwadi", "Kabza", "Amapiano")
    song2 = Song("Ukuthula", "Kabelo", "Kwapi")
    song3 = Song("Siyabonga", "Motha", "Oontz")


    print("Song Statistics:")
    print(Song.show_all_songs_info())

    print("\nIndividual Songs")
    print(f"{song1.name} by {song1.artist} ({song1.genre})")
    print(f"{song2.name} by (song2.artist) ({song2.genre})")
    print(f"{song3.name} by (song3.artist) ({song3.genre})")

if __name__ == "__main__":
    main()