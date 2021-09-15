from main import APIgenius


class PopularSong(APIgenius):
  ARTIST_NAME = input("Enter artist name:\n")

  artist = APIgenius.genius.search_artist(ARTIST_NAME, max_songs=3)
  page = 1
  songs = []
  while page:
      request = APIgenius.genius.artist_songs(artist.id,
                                              sort='popularity',
                                              per_page=50,
                                              page=page,
                                              )
      songs.extend(request['songs'])
      page = request['next_page']
  least_popular_song = APIgenius.genius.search_song(
      songs[-1]['title'], artist.name)
  print(least_popular_song.lyrics)
