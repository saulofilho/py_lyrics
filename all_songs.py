from main import APIgenius


class AllSongs(APIgenius):
    ARTIST_NAME = input("Enter artist name:\n")

    artist = APIgenius.genius.search_artist(ARTIST_NAME)
    artist.save_lyrics()

    print(artist.save_lyrics())
