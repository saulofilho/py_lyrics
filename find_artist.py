from main import APIgenius


class FindArtist(APIgenius):
    ARTIST_NAME = input("Enter artist name:\n")

    artist = APIgenius.genius.search_artist(
        ARTIST_NAME, max_songs=3, sort='title')

    print(artist.songs)
