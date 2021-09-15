from main import APIgenius


class FindSong(APIgenius):
  SONG_LYRIC = input("Enter song lyric:\n")

  request = APIgenius.genius.search_all(SONG_LYRIC)  # or search_lyrics
  for hit in request['sections'][2]['hits']:
      print(hit['result']['title'])
