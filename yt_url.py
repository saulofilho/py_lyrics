import json
from main import APIgenius


class YTUrl(APIgenius):
  with open('saved_file.json') as f:
      data = json.load(f)
  for song in data['songs']:
      links = song['media']
      if links:
          for media in links:
              if media['provider'] == 'youtube':
                  print(print(['song'] + ': ' + media['url']))
                  break


# ERROR
# >>> from yt_url import YTUrl
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/saulofilho/Development/_Experiments/py_lyrics/yt_url.py", line 5, in <module>
#     class YTUrl(APIgenius):
#   File "/home/saulofilho/Development/_Experiments/py_lyrics/yt_url.py", line 13, in YTUrl
#     print(print(['song'] + ': ' + media['url']))
# TypeError: can only concatenate list (not "str") to list
# >>>